import argparse
import math
import os
import subprocess
from typing import Sequence


def cfnguard_scan(
    rules_location: str,
    template_location: str,
    # show_summary: bool = False,
    # verbose: bool = False,
) -> int:
    try:
        retv = 0
        cmd_str = ("cfn-guard validate -r {0} --data {1}").format(rules_location, template_location)
        # if show_summary:
        #     cmd_str += " --show-summary all"
        # if verbose:
            # cmd_str += " --verbose"
        run_cmd = subprocess.run(
            cmd_str.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            encoding='utf-8',
            check=True,
        )
        # print(run_cmd.stdout)
        return retv
    except FileNotFoundError as e:
        raise Exception(f"cfn-guard not found.Please install it")
    except Exception as e:
        raise e


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(add_help=False)
    required: argparse.ArgumentGroup = parser.add_argument_group("required arguments")
    optional: argparse.ArgumentGroup = parser.add_argument_group("optional arguments")
    optional.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )
    # optional.add_argument(
    #     "--show-summary",
    #     action="store_true",
    # )
    required.add_argument(
        "-r",
        "--rules-location",
        required=True,
        help='Enforce all files are checked, not just staged files.',
    )
    required.add_argument(
        "-t",
        "--template-location",
        required=True,
        help='Location of the CloudFormation template',
    )
    # parser.add_argument(
    #     '--rules-location',
    #     type=str, default='./cfn-rules/*/*',
    #     help='Enforce all files are checked, not just staged files.',
    # )
    # parser.add_argument(
    #     '--template-location', type=str,
    #     default='./cdk.out/*.template.*',
    #     help='Location of the CloudFormation template',
    # )
    # parser.add_argument(
    #     '--show-summary', action='store_true',
    #     help='Show summary of results',
    # )
    # parser.add_argument(
    #     '--verbose', action='store_true',
    #     help='Show verbose output',
    # )
    args: argparse.Namespace = parser.parse_args()

    return cfnguard_scan(args.rules_location, args.template_location)


if __name__ == '__main__':
    raise SystemExit(main())