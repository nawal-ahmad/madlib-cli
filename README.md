[source used](https://stackoverflow.com/questions/40972805/python-capture-contents-inside-curly-braces/40972959)

**\{(.\*?)\}**

- > \{ matches the character { literally (case sensitive)
- > (.\*?) 1st Capturing Group
- > .\*? matches any character
- > \*? Quantifier — Matches between zero and unlimited times, as few times as possible, expanding as needed (lazy)
- > \} matches the character } literally (case sensitive)

[Pull Request Link](https://github.com/nawal-ahmad/madlib-cli/compare/lab3?expand=1)
