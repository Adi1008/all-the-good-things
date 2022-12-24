import shutil
import subprocess
import pandas as pd
import re

df = pd.read_csv("test_responses_5.csv")

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
    #f.write("\n\n")
    f.write("\n\n"+r"\begin{center}")
    messages = relevant_rows["Message:"]
    for index, message in messages.items():
        message = message.strip()
        message = message.replace("\n", "\n\n")
        #message = message.replace(r'"', "\n\n")
        message = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', message)
        f.write("\t\n"+message)
        f.write(" -- " + r"\textit{" + str(relevant_rows.at[index, "From:"]) + r"}" + "\n")
        f.write("\t\n"+r"\vspace{1cm}")
    #f.write("\n")
    f.write("\n"+r"\end{center}")

    # End .tex file
    f.write("\n\n"+r"\end{document}")

    # Close .tex file
    f.close()

    # Run pdflatex to create PDf file from .tex file
    subprocess.call(["pdflatex", filename])