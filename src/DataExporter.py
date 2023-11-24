class TextFileExporter:
    @staticmethod
    def export(path, data):
        records = set()
        with open(path, 'x') as file:

            file.write(str(data))

        return records