# all-the-good-things

In my high school orchestra program, All The Good Things was an event where people wrote kind messages to each other. It was one of the highlights of the year, and I still have all the messages people wrote to me. I think it'd be really cool to do it for our cohort, which is why I created this repository.

For this event, you are invited to reflect on the people in this cohort who have impacted your life and write them a message to let them know. Your message can be whatever length, tone, or style you want; just make sure to be kind and respectful overall.

**All members of the "Stanford ChemEs '27" Slack workspace are welcome to participate, including coterm/masters/SCPD students and PhD students in other departments.**

## Instructions

- Messages are due by **Tuesday, February 7, 2023**.
- Write messages to your friends through [this form](https://tinyurl.com/atgt2023).
  - In the `From:` field, write your name, or write “Anonymous” if you would prefer to stay anonymous.
  - In the `To:` field, select the name of the person you are writing your message to.
  - In the `Message:` field, write your message using the formatting guidelines in the next section.
  - Submit the form.
  - Repeat as many times as you'd like!

## Formatting

- **Bold** text by putting two asterisks on either side of it (`**your text here**`).
- *Italicize* text by putting one asterisk on either side of it (`*your text here*`).
- ~~Strike through~~ text by using the `\st{}` command (`\st{your text here}`).
- Typing quotation marks (`'` or `"`), percent signs (`%`), and pound signs (`#`) can be done normally, even though they are special characters in LaTeX.
- If you want to use an underscore outside of math mode (see below), you need to include a backslash before it
  - For example, typing `i\_like\_underscores` would appear in the final PDF as "i_like_underscores".
- After Eric's class, I think I've had enough math for a lifetime. If you want to, however, you can add math to your message using standard LaTeX.
  - For in-line math, put your math between one dollar sign on either side (`$a^2 + b^2 = c^2$`).
  - If you want your math on its own line, then use two dollar signs on each side (`$$a^2 + b^2 = c^2$$`).
  - You can use any math symbols you want, as long as they come from the `amsmath`, `amssymb`, or `braket` packages. If you want to add another package, let me know or create a pull request.

## Example input and output

See the `example` folder in this repository for an example input .csv file and its corresponding output .tex and .pdf files.

## Acknowledgments

- Eleanor, who gave me a lot of good feedback and advice for this project over winter break.
- Dhruva, whose `latex-exam` [repository](https://github.com/dkarkada/latex-exam) served as my starting point for this project.
