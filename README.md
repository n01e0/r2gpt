# ChatGPT in r2

## Installation

```bash
git clone git@github.com:n01e0/r2gpt /some/path/to/r2gpt
r2pm -i r2ghidra
python3 -m pip install -r /some/path/to/r2gpt/requirements.txt
echo '(askGPT func; "#!pipe python3 /some/path/to/r2gpt/r2gpt.py $0")' >> ~/.radare2rc
```

You need to set the API key to `OPENAI_API_KEY`.

## Usage

```
.(askGPT {{funcname}})
```
