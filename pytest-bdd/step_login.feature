@login
Feature: Login
    Scenario: Valid Login
        Given I visit the main page
        When I login with valid credentials
        Then I should be on the account page


    Scenario: Invalid Login
        Given I visit the main page
        When I login with invalid credentials
        Then I should see an error message