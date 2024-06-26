import json
import time
import pandas as pd
from tqdm import tqdm
from seleniumbase import SB

# Please update the project names of FlowGPT here.
# Complete name list is accessible at
# https://github.com/idllresearch/malicious-gpt/blob/main/malicious_LLM_name_list
df = pd.read_csv("malicious_LLM_applications_on_FlowGPT.csv")

flowgpt_malla_bot_names = df['name'].tolist()

# Visualize sleep bar
def sleepBar(seconds):
    for _ in tqdm(range(seconds)):
        time.sleep(1)


# Sign in FlowGPT with in 60 second (In this task, it is not necessary to sign in.)
def signin(sb):
    sb.uc_open_with_reconnect("https://flowgpt.com/")
    sleepBar(60)
    return sb


def dataCollecting(sb, names, outputfile):
    for name in names:
        sb.get("https://flowgpt.com/p/{}".format(name))
        sleepBar(10)

        targets = sb.find_elements('xpath', '//p[@class="overflow-hidden text-2sm font-normal text-fgMain-0"]')
        reviews = [target.text for target in targets]
        outputfile.write(json.dumps({"bot_name": name, "reviews": reviews}) + "\n")
        sleepBar(1)


def main():
    with SB(uc=True) as sb:
        browser = signin(sb)
        with open("./flowgpt-reviews.json", "w", encoding="utf8") as wf:
            dataCollecting(browser, flowgpt_malla_bot_names, wf)


if __name__ == '__main__':
    main()
