# all-the-good-things

All The Good Things is an event where people write notes to each other and submit them through Google Forms. This repository contains code used to generate the .tex and .pdf files for everyone's notes from the Google Form responses.

## Formatting guidelines:

- **Bold** text by putting two asterisks on either side of it (`**your text here**`)
- *Italicize* text by putting one asterisk on either side of it (`*your text here*`)
- ~~Strike through~~ text by using the `\st{}` command (`\st{your text here}`)
- "Quote" text (i.e., put it in quotation marks) by using the `\q{}` command (`\q{your text here}`). LaTeX uses ` and 
- After Eric's class, I think I've had enough math for a lifetime. If you want to, however, you can add math to your message using standard LaTeX. For in-line math, put your math between one dollar sign on either side (`$a^2 + b^2 = c^2$`). If you want your math on its own line, then use two dollar signs on each side(`$$a^2 + b^2 = c^2$$`)
- If you want to use an underscore outside of math mode, you need to include a blackslash before it (`\_`)