# all-the-good-things

In my high school orchestra program, All The Good Things was an event where people wrote kind notes to each other. It was one of the highlights of the year, and I still have all the messages people wrote to me.

I think it'd be really cool to do it for our cohort this year. This repository contains the code used to generate the .tex and .pdf files for everyone's notes from a .csv of Google Form responses.

## Logistics:

- Write messages to your friends through [this form](https://tinyurl.com/atgt2023).
- Messages are due by **Tuesday, February 7, 2023**.

## Formatting tips:

- **Bold** text by putting two asterisks on either side of it (`**your text here**`)
- *Italicize* text by putting one asterisk on either side of it (`*your text here*`)
- ~~Strike through~~ text by using the `\st{}` command (`\st{your text here}`)
- Typing quotation marks (`'` or `"`), percent signs (`%`), and pound signs (`#`) can be done normally, even though they are special characters in LaTeX
- After Eric's class, I think I've had enough math for a lifetime. If you want to, however, you can add math to your message using standard LaTeX. 
  - For in-line math, put your math between one dollar sign on either side (`$a^2 + b^2 = c^2$`)
  - If you want your math on its own line, then use two dollar signs on each side(`$$a^2 + b^2 = c^2$$`)
  - If you want to use an underscore outside of math mode, you need to include a backslash before it (`\_`)
  - You can use any math symbols you want, as long as they come from the `amsmath`, `amssymb`, or `braket` packages.

## Example input and output
See the `example` folder in this repository for an example input .csv file and its corresponding output .tex and .pdf files.