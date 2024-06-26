import json
import time
from tqdm import tqdm
import undetected_chromedriver as uc


# Please update the project names of FlowGPT here.
# Complete name list is accessible at
# https://github.com/idllresearch/malicious-gpt/blob/main/malicious_LLM_name_list
flowgpt_malla_bot_names = ["agpt-v7-jailbreak", "kawaii-girl"]


# Visualize sleep bar
def sleepBar(seconds):
    for _ in tqdm(range(seconds)):
        time.sleep(1)


# Initialize browser
def initUndetectedBrowser():
    return uc.Chrome()


# Sign in FlowGPT with in 60 second (In this task, it is not necessary to sign in.)
def signin():
    bot = initUndetectedBrowser()
    bot.get("https://flowgpt.com/")
    sleepBar(60)
    return bot


def dataCollecting(bot, names, outputfile):
    for name in names:
        bot.get("https://flowgpt.com/p/{}".format(name))
        sleepBar(10)

        targets = bot.find_elements('xpath', '//p[@class="overflow-hidden text-2sm font-normal text-fgMain-0"]')
        reviews = [target.text for target in targets]
        outputfile.write(json.dumps({"bot_name": name, "reviews": reviews}) + "\n")
        sleepBar(1)


def main():
    browser = signin()
    with open("./flowgpt-reviews.json", "w", encoding="utf8") as wf:
        dataCollecting(browser, flowgpt_malla_bot_names, wf)


if __name__ == '__main__':
    main()