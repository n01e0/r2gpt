import openai
import r2pipe
import sys
import os

openai.api_key = os.environ['OPENAI_API_KEY']

def createR2Pipe():
    try:
        pipe = r2pipe.open()
        pipe.cmd('a')
        return pipe
    except:
        print('Unexpected error')
        return None


def askGPT(func: str) -> str:
    resp = openai.ChatCompletion.create(
        model="o4-mini",
        messages=[
            {"role": "user", "content": "How does this function work"},
            {"role": "user", "content": func}
        ]
    )

    return resp['choices'][0]['message']['content']


def decompile(func: str, pipe) -> str:
    return pipe.cmd(f'pdg @{func}')


def main(func):
    pipe = createR2Pipe()
    dec = decompile(func, pipe)

    resp = askGPT(dec)
    print(resp)

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        print(f'Usage: {argv[0]} function (addr|name)')
        exit(1)
    func = sys.argv[1]
    main(func)
