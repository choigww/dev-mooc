import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('../chromedriver', options=options)
#url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year=2019&page=1'
titles = []
reviews = []
try:
    for l in range(1,4):
        url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year=2019&page={}'.format(l)
        for i in range(1,21):
            try:
                driver.get(url)
                time.sleep(1)
                movie_title_xpath = '//*[@id="old_content"]/ul/li[{}]/a'.format(i)
                title = driver.find_element_by_xpath(movie_title_xpath).text
                print(title)
                #titles.append(title)
                driver.find_element_by_xpath(movie_title_xpath).click()
                time.sleep(1)
                try:
                    btn_review_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a/em'
                    driver.find_element_by_xpath(btn_review_xpath).click()
                    time.sleep(1)
                    print('debug1')
                    try:
                        review_len_path = '//*[@id="reviewTab"]/div/div/div[2]/span/em'
                        review_len = driver.find_element_by_xpath(review_len_path).text
                        review_len = review_len.replace(',', '')
                        review_len = int(review_len)
                        try:
                            for j in range(1, (review_len - 1) // 10 + 2):
                                review_page_xpath = '//*[@id="pagerTagAnchor{}"]'.format(j)
                                driver.find_element_by_xpath(review_page_xpath).click()
                                time.sleep(1)
                                for k in range(1, 11):
                                    review_title_xpath = \
                                        '//*[@id="reviewTab"]/div/div/ul/li[{}]/a/strong'.format(k)
                                    try:
                                        driver.find_element_by_xpath(
                                            review_title_xpath).click()
                                        time.sleep(1)
                                    except:
                                        print('except3')
                                    try:
                                        review = driver.find_element_by_xpath(
                                            '//*[@id="content"]/div[1]/div[4]/div[1]/div[4]').text
                                        titles.append(title)
                                        reviews.append(review)
                                        driver.back()
                                        time.sleep(1)
                                    except:
                                        driver.back()
                                        time.sleep(1)
                                        print('except2')
                            print(len(reviews))
                        except:
                            driver.back()
                            time.sleep(1)
                            print('except1')


                    except:
                        print('except4')
                except:
                    print('except3')
            except:
                print('except2')

        print(len(titles))
    df_review = pd.DataFrame({'title':titles, 'review':reviews})
    df_review.to_csv('./crawling/movie_review_2019_3.csv')
except:
    print('except1')
finally:
    driver.close()


