Feature: Compose Function to send email

  Scenario: composing email
    Given launch browser
    When gmail homepage is open
    And  user email as email
    And click next button
    And user password as password
    And next button to login
    Then user must login
    And click on compose link
    And input data in subject
    And input message in email