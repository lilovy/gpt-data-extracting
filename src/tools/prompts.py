
class LoadPrompt(object):
    def __init__(
        self,
        prompt_file: str,
        ):
        self.__prompt = self.__load_prompt(prompt_file)

    def __load_prompt(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def __str__(self):
        return self.__prompt


if __name__ == "__main__":
    print(LoadPrompt('prompt_extract_data.txt'))