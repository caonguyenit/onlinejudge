import os

from django.core.management.base import BaseCommand, CommandError

from judge.models import Contest, ContestParticipation
from judge.models.submission import Submission


class Command(BaseCommand):
    help = 'export contest submissions'

    def add_arguments(self, parser):
        parser.add_argument('key', help='contest key')
        parser.add_argument('output', help='output directory')

    def handle(self, *args, **options):
        contest_key = options['key']
        output_file = options['output']

        contest = Contest.objects.filter(key=contest_key).first()
        print(contest)
        if contest is None:
            raise CommandError('contest not found')

        if os.path.exists(output_file):
            raise CommandError('output file already exists')

        users = contest.users.filter(virtual=ContestParticipation.LIVE).select_related('user__user')
        problems = contest.contest_problems.order_by('order')

        head = ['username']

        for problem in problems:
            head.append(problem.problem.code)

        rows = [','.join(head)]
        # return

        user_count = 0
        submission_count = 0


        for user in users:
            user_count += 1

            username = user.user.user.username

            submissions = user.submissions.exclude(submission__result__in=('IE', 'CE'))
            result = {

            }
            for submission in submissions:
                cases = submission.submission.test_cases.order_by('case')
                result_string = ''.join(['1' if case.status == 'AC' else '0' for case in cases])
                result[submission.submission.problem.id] = result_string
            row = [username]
            for problem in problems:
                row.append('"' + result.get(problem.problem.id, '0') + '"')
            rows.append(','.join(row))

        open(output_file, 'w').write('\n'.join(rows))
        print(f'Exported {submission_count} submissions by {user_count} users')
