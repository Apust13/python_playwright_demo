from playwright.sync_api import Page, expect

from elements.button import Button
from elements.checkbox import CheckBox
from elements.input import Input
from elements.radio_button import RadioButton
from elements.select import Select
from elements.text import Text
from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.form_title = Text(page, '.login-form>.title', 'Account information')
        self.gender_mr_radio = RadioButton(page, '#id_gender1', 'Mr.')
        self.gender_mrs_radio = RadioButton(page, '#id_gender2', 'Mrs.')

        self.name_input = Input(page, '#name', 'Name')
        self.email_input = Input(page, '#email', 'Email')
        self.password_input = Input(page, '#password', 'Password')

        self.days_dropdown = Select(page, '#days', 'Day')
        self.months_dropdown = Select(page, '#months', 'Month')
        self.years_dropdown = Select(page,'#years', 'Year')

        self.newsletter_checkbox = CheckBox(page,'#newsletter', 'Newsletter')
        self.receive_special_offers_checkbox = CheckBox(page, '#optin', 'Receive special offers')

        self.first_name_input = Input(page, '#first_name', 'First name')
        self.lastname_input = Input(page,'#last_name', 'Last name')
        self.company_input = Input(page,'#company', 'Company')
        self.address_input = Input(page,'#address1', 'Address')
        self.address2_input = Input(page,'#address2', 'Address 2')

        self.country_dropdown = Select(page, '#country', 'Country')
        self.state_input = Input(page,'#state', 'State')
        self.city_input = Input(page,'#city', 'City')
        self.zipcode_input = Input(page,'#zipcode', 'Zipcode')
        self.mobile_number_input = Input(page,'#mobile_number', 'Mobile number')
        self.create_account_button = Button(page,'[data-qa="create-account"]', 'Create Account')



    def check_signup_form_visible(self, name: str, email: str):
        self.form_title.check_visible()
        self.form_title.check_have_text('ENTER ACCOUNT INFORMATION', ignore_case=True)

        self.name_input.check_have_value(name)
        self.email_input.check_have_value(email)

    def fill_signup_form(
            self,
            title: str,
            password: str,
            day_of_birth: str,
            month_of_birth: str,
            year_of_birth: str,
            first_name:str,
            last_name:str,
            company:str,
            address:str,
            country: str,
            state: str,
            city: str,
            zipcode: str,
            mobile_number: str,
            address_2: str = '',
            signup_for_newsletter: bool = True,
            receive_special_offers: bool = True,
    ):
        if 'mrs' in title.lower():
            self.gender_mrs_radio.click()
        else:
            self.gender_mr_radio.click()

        self.password_input.fill(password)

        self.days_dropdown.select(day_of_birth)
        self.months_dropdown.select(month_of_birth)
        self.years_dropdown.select(year_of_birth)

        if signup_for_newsletter:
            self.newsletter_checkbox.check()
            self.newsletter_checkbox.check_is_checked()

        if receive_special_offers:
            self.receive_special_offers_checkbox.check()
            self.receive_special_offers_checkbox.check_is_checked()

        self.first_name_input.fill(first_name)
        self.lastname_input.fill(last_name)
        self.company_input.fill(company)

        self.address_input.fill(address)

        if address_2:
            self.address2_input.fill(address_2)

        self.country_dropdown.select(country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_number_input.fill(mobile_number)

    def click_create_account_button(self):
        self.create_account_button.click()

