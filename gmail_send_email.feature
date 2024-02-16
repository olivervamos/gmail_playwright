Feature: Gmail Send Email

  Scenario: Send email to adress from contacts
    Given I am on the Gmail login page
    When I enter valid username and password
    Then I should be logged in successfully
    When I click on the Contacts icon
    And I click on the contact
    And I click on the Send email icon
    And I fill subject
    And I click on the Send button
    Then Message sent should be visible
    When I click on the profile icon
    And I click on the Sign out button
    Then I should be logged out successfully

Scenario: Send email with attachement to adress from contacts
    Given I am on the Gmail login page
    When I enter valid username and password
    Then I should be logged in successfully
    When I click on the Contacts icon
    And I click on the contact
    And I click on the Send email icon
    And I fill subject
    And I attach file
    And I click on the Send button
    Then Message sent should be visible
    When I click on the profile icon
    And I click on the Sign out button
    Then I should be logged out successfully