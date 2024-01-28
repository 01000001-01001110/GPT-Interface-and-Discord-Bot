import axios from 'axios';
import cheerio from 'cheerio';

async function fetchData(url) {
  try {
    const response = await axios.get(url);
    const data = response.data;
    const $ = cheerio.load(data);
    const extractedData = [];

    // Iterate over each article element
    $('article').each((index, element) => {
      // Updated selector to target <h2> inside <figcaption>
      const title = $(element).find('figcaption h2').text().trim();
      const description = $(element).find('.biography').text().trim(); // Updated selector for description
      const imageUrl = $(element).find('img').attr('src');
      const biography = $(element).find('.biography').text().trim();
      const features = $(element).find('.features div').map((_, el) => $(el).text().trim()).get();
      const detailsUrl = $(element).find('.showDetails a').attr('href');

      const fullDetailsUrl = detailsUrl.startsWith('http') ? detailsUrl : new URL(detailsUrl, url).href;

      extractedData.push({ title, description, imageUrl, biography, features, detailsUrl: fullDetailsUrl });
    });

    return extractedData;
  } catch (error) {
    console.error(`There was an error fetching the data: ${error}`);
    return null;
  }
}

export default fetchData;
