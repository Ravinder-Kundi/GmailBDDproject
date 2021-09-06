Feature: Gmail Login

  Background: common steps
    Given launch browser
    When gmail homepage is open

  Scenario: gmail home page
    Then confirm Gmail title


  Scenario: login with valid cradential
    When user email as email
    And click next button
    And user password as password
    And next button to login
    Then user must login

  Scenario Outline: : login with multi parameters
    When user email as "<email>"
    And click next button
    And user password as "<password>"
    And next button to login
    Then user must login

    Examples:
      | email                 | password  |
      | aaaaabbb002@gmail.com | ababab002 |
      | aaaaabbb002@gmail.com | ababab001 |
