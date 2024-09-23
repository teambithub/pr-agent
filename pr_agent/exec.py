import argparse
import asyncio
import json
import os


from pr_agent.algo.ai_handlers.litellm_ai_handler import LiteLLMAIHandler

from pr_agent.config_loader import get_settings
from pr_agent.log import setup_logger, LoggingFormat

from pr_agent.tools.pr_code_suggestions import PRCodeSuggestions
from pr_agent.tools.pr_generate_labels import PRGenerateLabels
from pr_agent.tools.pr_reviewer import PRReviewer


log_level = os.environ.get("LOG_LEVEL", "DEBUG")
setup_logger(level=log_level, fmt=LoggingFormat.CONSOLE)


def run():
    get_settings().set("CONFIG.CLI_MODE", False)
    get_settings().set("CONFIG.VERBOSITY_LEVEL", 2)

    async def inner():

        pr_url = "https://github.com/teambithub/git-service/pull/33"
        ai_handler = LiteLLMAIHandler  # will be initialized in run_action
        obj = PRReviewer(pr_url=pr_url, ai_handler=ai_handler)
        await asyncio.create_task(obj.run())
        return obj.data if hasattr(obj, "data") else None

    result = asyncio.run(inner())
    if result:
        print('---------------------------- RESULT ----------------------------')
        print(json.dumps(result, indent=True))
        print('-------------------------- END RESULT --------------------------')
    else:
        print('>>>> NO RESULT')


if __name__ == '__main__':
    run()
