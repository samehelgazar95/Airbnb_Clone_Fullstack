$('document').ready(function () {
  const selectedStates = {};
  const selectedCities = {};
  const selectedAmenities = {};
  let locations = [];

  function toggleHeaderContent(headerPath, selectedItems) {
    $(headerPath).text(selectedItems);
    if ($.isEmptyObject(selectedItems)) $(headerPath).html('&nbsp;');
  }

  $('.amenities input').click(function () {
    if (this.checked) {
      selectedAmenities[this.dataset.name] = this.dataset.id;
    } else {
      delete selectedAmenities[this.dataset.name];
    }
    toggleHeaderContent('.amenities h4', Object.keys(selectedAmenities));
  });

  $('.locations .state_container input').click(function () {
    if (this.checked) {
      selectedStates[this.dataset.name] = this.dataset.id;
      locations.push(this.dataset.name);
    } else {
      delete selectedStates[this.dataset.name];
      let idx = locations.indexOf(this.dataset.name);
      locations.splice(idx, 1);
    }
    toggleHeaderContent('.locations h4', locations);
  });

  $('.locations .city_container input').click(function () {
    if (this.checked) {
      selectedCities[this.dataset.name] = this.dataset.id;
      locations.push(this.dataset.name);
    } else {
      delete selectedCities[this.dataset.name];
      let idx = locations.indexOf(this.dataset.name);
      locations.splice(idx, 1);
    }
    toggleHeaderContent('.locations h4', locations);
  });

  $.getJSON('http://0.0.0.0:5001/api/v1/status/', (body) => {
    if (body.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });

  function validateResponse(response) {
    if (!response.ok)
      throw new Error(`userResponse error!, status: ${response.status}`);
  }

  const filteredIds = {};
  $('.filters button').click(async function (event) {
    event.preventDefault();
    $('.places').text('');
    filteredIds.states = Object.values(selectedStates);
    filteredIds.cities = Object.values(selectedCities);
    filteredIds.amenities = Object.values(selectedAmenities);

    try {
      $('html').css({ cursor: 'wait' });
      const placesResponse = await fetch(
        'http://0.0.0.0:5001/api/v1/places_search/',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(filteredIds),
        }
      );
      validateResponse(placesResponse);

      let places = await placesResponse.json();
      let allArticlesHTML = ``;

      for (const place of places) {
        const userResponse = await fetch(
          `http://0.0.0.0:5001/api/v1/users/${place.user_id}`
        );
        validateResponse(userResponse);
        const reviewsResponse = await fetch(
          `http://0.0.0.0:5001/api/v1/places/${place.id}/reviews`
        );
        validateResponse(reviewsResponse);

        let user = await userResponse.json();
        let reviews = await reviewsResponse.json();

        let reviewsList = '';
        if (reviews.length > 0) {
          for (let i = 0; i < reviews.length && i < 3; i++) {
            let date = new Date(String(reviews[i].created_at));
            reviewsList += `
                      <li>
                      <p><b>Review at: ${date.getFullYear()}, ${
              date.getMonth() + 1
            }</b></p>
                      <p>${reviews[i].text}</p>
                      </li>
                      `;
          }
        } else {
          reviewsList = `<li>No reviews to show</li>`;
        }
        let article = `<article>
                          <div class="title_box">
                            <h2>${place.name}</h2>
                            <div class="price_by_night">$ ${
                              place.price_by_night
                            }</div>
                          </div>
                          <div class="information">
                              <div class="max_guest">${place.max_guest} Guest${
          place.max_guest != 1 ? 's' : ''
        }</div>
                              <div class="number_rooms">${
                                place.number_rooms
                              } Bedroom${
          place.number_rooms != 1 ? 's' : ''
        }</div>
                              <div class="number_bathrooms">${
                                place.number_bathrooms
                              } Bathroom${
          place.number_bathrooms != 1 ? 's' : ''
        }</div>
                          </div>
                          <div class="user">
                              <b>Owner: </b>${user.first_name} ${user.last_name}
                          </div>
                          <div class="description"><p>${
                            place.description
                          }</p></div>
                          <div class="amenities">
                            <div class=reviews>
                                      <h2>Reviews</h2>
                                      <ul>
                                          ${reviewsList}
                                      </ul>
                            </div>
                          </div>
                        </article>`;

        allArticlesHTML += article;
      }
      $('.places').html(allArticlesHTML);
      $('html').css({ cursor: 'default' });
    } catch (err) {
      console.error('There was a problem with the fetch operation:', error);
    }
  });
});
