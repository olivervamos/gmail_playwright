Feature: Gmail Login and Logout

  Scenario: Successful login and logout
    Given I am on the Gmail login page
    When I enter valid username and password
    Then I should be logged in successfully
    When I click on the profile icon
    And I click on the Sign out button
    Then I should be logged out successfully