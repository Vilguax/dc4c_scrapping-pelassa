import requests as r
from bs4 import BeautifulSoup
import csv

with open('result.csv', 'w', newline='') as csvfile:
    header_csv = ['Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Percentage', 'GF', 'GA', 'Difference']
    writer = csv.DictWriter(csvfile, fieldnames=header_csv)
    
    writer.writeheader()

    for i in range(10):
        url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}'

        response = r.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        teams_data = soup.find_all('tr', class_='team')

        for team in teams_data:
            name = team.find('td', class_='name')
            year = team.find('td', class_='year')
            wins = team.find('td', class_='wins')
            losses = team.find('td', class_='losses')
            ot_losses = team.find('td', class_='ot-losses')
            pct_text_success = team.find('td', class_='pct text-success')
            gf = team.find('td', class_='gf')
            ga = team.find('td', class_='ga')
            diff_text_success = team.find('td', class_='diff text-success')

            if diff_text_success and int(diff_text_success.text.strip()) > 0 and ga and int(ga.text.strip()) <= 300:
                writer.writerow({'Name': name.text.strip() if name else 'N/A',
                                 'Year': year.text.strip() if year else 'N/A',
                                 'Wins': wins.text.strip() if wins else 'N/A',
                                 'Losses': losses.text.strip() if losses else 'N/A',
                                 'OT Losses': ot_losses.text.strip() if ot_losses else 'N/A',
                                 'Percentage': pct_text_success.text.strip() if pct_text_success else 'N/A',
                                 'GF': gf.text.strip() if gf else 'N/A',
                                 'GA': ga.text.strip() if ga else 'N/A',
                                 'Difference': diff_text_success.text.strip() if diff_text_success else 'N/A'})