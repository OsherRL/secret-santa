# secret-santa
[![python-flake8][flake8-img]][flake8-url]

It's secret santa, but with unit tests!

## Compatibility
Python 3 is required (tested on python 3.8).

Currently only [gmail][gmail] addresses are supported and an [App Password][gmail-app-password] will be required.

## Linux Setup

Clone repository:

`git clone https://github.com/OsherRL/secret-santa.git`

Navigate into project directory:

`cd secret-santa`

Create python virtual environment:

`python3 -m venv venv`

Activate virtual environment:

`source venv/bin/activate`

Install required packages using pip:

`pip install -r requirements.txt`

Run `main.py` and supply a participant list as a [CSV][csv-docs] file:

`python main.py <path_to_participant_list>`

Finally, provide your name and email details when prompted and emails will be sent off to the participants informing them who they will be choosing gifts for.

## Formatting of Participant List File
The participant list should be formatted as a csv file with each row containing a participants name and email address. 

Example:

````
person1,person1@email.com
person2,person2@email.com
person3,person3@email.com
...
person50,person50@email.com
````


## Contributing

1. Fork it (https://github.com/OsherRL/secret-santa/fork)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License
This software is distributed under the [MIT License](LICENSE)


<!-- Markdown link & img dfn's -->
[flake8-img]: https://img.shields.io/badge/code%20style-flake8-brightgreen.svg?style=flat
[flake8-url]: https://flake8.pycqa.org/en/latest/

[csv-docs]: https://tools.ietf.org/html/rfc4180

[gmail]: https://www.google.com/gmail
[gmail-app-password]: https://support.google.com/accounts/answer/185833?hl=en
