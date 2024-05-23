import re
import zipfile


class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.text = self.read_text_from_file()

    def read_text_from_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

    def analyze_text(self):
        text = self.text
        sentences = re.split(r"[.!?]", text)
        sentences_count = len(sentences) - 1  # empty string
        narr_sentences = 0
        interrogative_sentences = 0
        imperative_sentences = 0

        narr_sentences = re.findall(r'[^\.\?!]*\.+', text)
        narr_sentences_count = len(narr_sentences)
        imperative_sentences = re.findall(r'[^\.\?!]*!+', text)
        imperative_sentences_count = len(imperative_sentences)
        interrogative_sentences = re.findall(r'[^\.\?!]*\?+', text)
        interrogative_sentences_count = len(interrogative_sentences)

        # Average sentence length
        total_sentence_length = sum(len(sentence.split()) for sentence in sentences)
        average_sentence_length = total_sentence_length / sentences_count

        # Average word length
        words = re.findall(r"\b\w+\b", text)
        total_word_length = sum(len(word) for word in words)
        average_word_length = total_word_length / len(words)

        # Search smiles
        smiles = re.findall(r"[:;]-*[(\[)\]]+", text)
        num_smiles = len(smiles)

        return (
            sentences_count,
            narr_sentences_count,
            interrogative_sentences_count,
            imperative_sentences_count,
            average_sentence_length,
            average_word_length,
            num_smiles,
        )


    def find_all_caps(self):
        text = self.text
        all_caps = re.findall(r"[A-Z]", text)
        return all_caps

    def replace_sequence(self):
        text = self.text
        replaced_text = re.sub(r"(\b\w*a*\w*ab\w*bc\w*c*\w*)", "qqq", text)
        return replaced_text

    def max_length_words(self):
        text = self.text
        words = re.findall(r"\b\w+\b", text)
        max_length = max(len(word) for word in words)
        max_length_words = [word for word in words if len(word) == max_length]
        return len(max_length_words),max_length

    def words_followed_by_punctuation(self):
        text = self.text
        word_punctuation = re.findall(r"\b\w+[.,]", text)
        return word_punctuation

    def longest_word_ending_with_e(self):
        text = self.text
        words = re.findall(r"\b\w+\b", text)
        longest_word = ""
        for word in words:
            if word.endswith("e") and len(word) > len(longest_word):
                longest_word = word
        return longest_word

    def archive(self):
        with zipfile.ZipFile("D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task2//archive.zip", "w") as z:
            z.write(self.filename)
        with zipfile.ZipFile("D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task2//archive.zip", "r") as z:
            return z.getinfo(self.filename)


def task2_run():
    a = TextAnalyzer('task2/file.txt')
    info = a.archive()
    (
        sentences_count,
        narr_sentences,
        interrogative_sentences,
        imperative_sentences,
        average_sentence_length,
        average_word_length,
        num_smiles,
    ) = a.analyze_text()
    max_length_words_count, max_length = a.max_length_words()
    print(
        f"--Sentences count: {sentences_count}\n"
        f"--Narrative sentences count: {narr_sentences}\n"
        f"--Interrogative sentences count: {interrogative_sentences}\n"
        f"--Imperative sentences count: {imperative_sentences}\n"
        f"--Average word length: {average_sentence_length}\n"
        f"--Average sentence length: {average_word_length}\n"
        f"--Smileys count: {num_smiles}\n"
        f"--All capital letters: {a.find_all_caps()}\n"
        f"--Text after sequence replacement:\n {a.replace_sequence()}\n"
        f"--Number of maximum length words: {max_length_words_count}\nMaximum word length: {max_length}\n"
        f"--Words followed by punctuation: {a.words_followed_by_punctuation()}\n"
        f"--Longest word that ends with 'e': {a.longest_word_ending_with_e()}\n"
    )
