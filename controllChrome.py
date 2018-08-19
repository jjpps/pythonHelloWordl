import unittest
import selenium
from selenium import webdriver
#using chrome

#drive = webdriver.Chrome()
drive = webdriver.Chrome(r"C:\Users\Usuario\Documents\Projedos Git\python\pythonHelloWordl\chromedriver.exe")

drive.get("https://www.facebook.com.br")

