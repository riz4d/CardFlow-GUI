# CardFlow-GUI

CardFlow-GUI is a user-friendly application for generating credit card details based on brand and country specifications. This graphical user interface (GUI) tool is designed to help developers and testers simulate credit card data for various testing purposes. Leveraging a dataset of Bank Identification Numbers (BINs), CardFlow-GUI ensures the generated credit card numbers are valid and realistic.

## Features

- **Brand Selection**: Generate credit card numbers for popular brands such as Visa, MasterCard, American Express, and more.
- **Country Selection**: Specify the country for which you need the credit card details.
- **Custom Quantity**: Generate a custom number of credit card details in one go.
- **Validation**: Utilizes a dataset of BINs to validate and generate realistic credit card numbers.
- **User-Friendly Interface**: Simple and intuitive GUI for ease of use.

### Why
  - Why do some of use fake credit cards?<br><br>
    Using fake credit cards to bypass free trials might appear advantageous to users seeking to access premium services without cost, offering temporary benefits such as saving money and experiencing full features of a            product or service. This exploitation can provide insight into various services without financial commitment, helping users evaluate the product's value before making a purchase decision.

  - How Fake Credit Cards Can Be Used for Free Trials?<br>
    - No CVV Verification:<br>
    Some services may skip CVV verification for free trials to reduce friction during the sign-up process.
    Fraudsters exploit this by using generated or stolen card numbers.<br>
    - Algorithm-Based Generation: <br>Generate valid-looking card numbers. These numbers might pass initial checks if the service does not validate CVV or run authorization checks.<br>
    - Stolen Card Data: <br>Stolen credit card details from data breaches can be used. Even without the CVV, if the card number and expiry date are valid, the system might accept it.<br>

    
### Dataset
CardFlow-GUI uses a comprehensive dataset of BINs to ensure the generated credit card numbers are valid and adhere to real-world standards. The dataset is included in the project and is automatically used during the generation process.
### Setup

1. Clone the Repository

    ```sh
    git clone https://github.com/riz4d/CardFlow-GUI.git
    ```
    ```sh
    cd CardFlow-GUI
    ```

2. Install Dependencies

    ```sh
    pip install -r requirements.txt
    ```
3. Run App

    ```sh
    python3 app.py
    ```

### Related Repo
- CardFlow-CLI: Command-line interface version of CardFlow-GUI for generating credit card details.
- [CardFlow CLI Repo](https://github.com/riz4d/Card-Flow)

### Issues 

[Submit Issues](https://github.com/riz4d/CardFlow-GUI/issues)

### Disclaimer
This project cardflow is provided solely for educational purposes. Any use of the generated credit card information for fraudulent activities or illegal purposes is strictly prohibited. We do not endorse or encourage any misuse of the generated data. Users are solely responsible for their actions and any consequences that may arise from the misuse of this tool. By using this credit card generator, you agree to use it responsibly and acknowledge that we are not liable for any damages or legal issues resulting from its misuse.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Acks

If you have any questions or feedback, please reach out to us at cardflow@rizad.me
