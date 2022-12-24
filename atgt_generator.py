import shutil
import subprocess
import pandas as pd
import re

# Clean up input and allow for bolding, italics, etc.
# Input: raw form of message
# Output: cleaned-up message with LaTeX commands for bold, italics, etc.
def clean_input(message):
    # Get rid of leading/trailing whitespaces
    message = message.strip()
    # Adjust the number of newlines so that the rendered PDF looks like how it's supposed to
    message = message.replace("\n", "\n\n")
    # Add LaTeX command for bold
    message = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', message)
    # Add LaTeX command for italics
    message = re.sub(r'\*(.+?)\*', r'\\textit{\1}', message)

    return message

# Load responses
df = pd.read_csv("test_responses.csv")

# Get names of all recipients
recipient_names = df.iloc[:,2].unique()

# Generate the .tex file and PDF for each recipient
for name in recipient_names:
    # Select all the rows with messages to this person
    relevant_rows = df[df.iloc[:,2] == name]

    # Create .tex file for this person
    filename = name.split()[0] + ".tex"
    shutil.copyfile("foundation.tex", filename)
    f = open(filename, 'a')

    # Add title to .tex file
    f.write("\n\n"+r"\begin{center}")
    f.write("\n"+r"{\Huge " + name + r"}")
    f.write("\n"+r"\end{center}")
    f.write("\n"+r"\vspace{1cm}")

    # Iterate through all the messages for this person and add them to the .tex file
    f.write("\n\n"+r"\begin{center}")
    messages = relevant_rows["Message:"]
    for index, message in messages.items():
        message = clean_input(message)
        f.write("\n"+message)
        f.write(" -- " + r"\textit{" + str(relevant_rows.at[index, "From:"]) + r"}" + "\n")
        f.write("\n"+r"\vspace{1cm}"+"\n")
    f.write("\n"+r"\end{center}")

    # End .tex file
    f.write("\n\n"+r"\end{document}")

    # Close .tex file
    f.close()

    # Run pdflatex to create PDf file from .tex file
    subprocess.call(["pdflatex", filename])