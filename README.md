# PokerNow Flask Ledger API

This is a simple Flask API for retrieving ledger information and performing transaction calculations for PokerNow links.

## Installation

1. Clone the repository to your local machine:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd flask-ledger-api
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Access the endpoints using a web browser or API client:

- **GET /get_ledger**: Retrieve the ledger information. Append `?url=<POKERNOW_LINK>` to the endpoint URL, replacing `<POKERNOW_LINK>` with the PokerNow link (e.g., `http://127.0.0.1:5000/get_ledger?url=https://www.pokernow.club/games/pgldCJeNJgBxwUMm13HxJTquy`).

- **GET /get_transactions**: Retrieve the minimum transactions. Append `?url=<POKERNOW_LINK>` to the endpoint URL, replacing `<POKERNOW_LINK>` with the PokerNow link (e.g., `http://127.0.0.1:5000/get_transactions?url=https://www.pokernow.club/games/pgldCJeNJgBxwUMm13HxJTquy`).

- **GET /get_payment_strings**: Retrieve the payment strings indicating who pays whom. Append `?url=<POKERNOW_LINK>` to the endpoint URL, replacing `<POKERNOW_LINK>` with the PokerNow link (e.g., `http://127.0.0.1:5000/get_payment_strings?url=https://www.pokernow.club/games/pgldCJeNJgBxwUMm13HxJTquy`).

## Development

- Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
