import json
import jsonlines
import sys
import os
import csv
import click



@click.command()
@click.option('--filename', prompt='File to process')
@click.option('--columns', default=1, help='One column for uploading documents, two for question/answer pairs.')
@click.option('--skip-header/--no-skip-header', default=False)
def transform(filename, columns, skip_header):
	"""Simple program that greets NAME for a total of COUNT times."""
	arguments = sys.argv
	input_file_name = filename

	if input_file_name.endswith(".json"):
		with open(input_file_name) as input_file, jsonlines.open(input_file_name+'.out.jsonl', mode='w') as writer:
			data = json.load(input_file)
			for message in data:
				message_content = message["content"]
				writer.write({'text': message_content})
	elif input_file_name.endswith(".csv"):
		with open(input_file_name) as fp, jsonlines.open('makerdao_faq_document_gpt3.jsonl', mode='w') as writer:
			reader = csv.reader(fp, delimiter=",", quotechar='"')
			# next(reader, None)  # skip the headers
			data_read = [row for row in reader]
			for row in data_read:
				message_content = row[0]
				writer.write({'text': message_content})

	else:
		sys.exit("Unsopported file format")


	print("Transformed input data to GPT3 document format")


if __name__ == '__main__':
	transform()

