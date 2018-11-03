@navigation
Feature: Let me google 'appium' for you

  Scenario: Google search works correctly
    When User opens google
    Then Types appium in search box