export default function Info() {
    return (
      <div>
          <nav>
            <div class="nav nav-tabs nav-fill"
                id="nav-tab"
                role="tablist">
              <a class="nav-item nav-link active"
                id="nav-home-tab"
                data-toggle="tab"
                href="#nav-home"
                role="tab"
                aria-controls="nav-home"
                aria-selected="true">Mapa</a>
              <a class="nav-item nav-link"
                id="nav-profile-tab"
                data-toggle="tab"
                href="#nav-profile"
                role="tab"
                aria-controls="nav-profile"
                aria-selected="false">Partidos</a>
              <a class="nav-item nav-link"
                id="nav-contact-tab"
                data-toggle="tab"
                href="#nav-contact"
                role="tab"
                aria-controls="nav-contact"
                aria-selected="false">Puntaje</a>
            </div>
          </nav>
          <div class="tab-content"
              id="nav-tabContent">
            <div class="tab-pane fade show active"
                id="nav-home"
                role="tabpanel"
                aria-labelledby="nav-home-tab"
            >
              <div class="container-fluid mt-3">
                <div class="row">
                  <div class="col-12 justify-content-center">
                    {/* {% if university %} */}
                      <div class="row justify-content-center mb-4">
                        {/* {% if university.logo %} */}
                          <img class="img-fluid"
                              src="{{ university.logo.url }}"
                              alt="Logo Sede"
                              style={{maxWidth: "100px"}}/>
                        {/* {% endif %} */}
                        <h3 class="my-auto">
                          [UNIVERSITY]
                        </h3>
                      </div>
                      {/* {% if university.map %} */}
                      <div class="row">
                        <img class="img-fluid"
                            src="{{ university.map.url }}"
                            alt="Mapa Sede"
                            style={{maxWidth: "98%"}}/>
                      </div>
                      {/* {% else %} */}
                        <h1 class="text-center mt-5">
                          Aun no se ha cargado un mapa de la sede.
                        </h1>
                      {/* {% endif %} */}
                    {/* {% else %} */}
                      <h1 class="text-center mt-5">
                        Aun no se ha determinado la universidad sede.
                      </h1>
                    {/* {% endif %} */}
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade"
                id="nav-profile"
                role="tabpanel"
                aria-labelledby="nav-profile-tab"
            >
              <div class="container-fluid">
                <div class="table-responsive col-md-10 offset-md-1 mt-4">
                  <table id="dt-select"
                        class="table table-striped table-bordered table-hover"
                        cellspacing="0"
                        width="100%">
                    <thead>
                      <tr>
                        <th>Fecha</th>
                        <th>Hora</th>
                        <th>Lugar</th>
                        <th>Deporte</th>
                        <th>Participantes</th>
                        <th>Estado</th>
                      </tr>
                    </thead>
                    <tbody>
                      {/* {% for match in matches %} */}
                        <tr>
                          <td>[DD-MM-YY]</td>
                          <td>[HH:mm]</td>
                          <td>[LOCATION]</td>
                          <td>[SPORT]</td>
                          <td>
                            <ul>
                              {/* {% for team_match in match.teams.all %} */}
                              <li>[UNI]</li>
                              {/* {% endfor %} */}
                            </ul>
                          </td>
                          <td>[STATE]</td>
                        </tr>
                      {/* {% endfor %} */}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="tab-pane fade"
                id="nav-contact"
                role="tabpanel"
                aria-labelledby="nav-contact-tab"
            >
              <div class="container-fluid mt-4">
                <div class="row w-100 justify-content-around">
                  <div class="col-md-5">
                    <h1>
                      Tabla General
                    </h1>
                    <div class="mt-4">
                      <table id="dt-general"
                            class="table table-striped table-bordered table-hover"
                            cellspacing="0"
                            width="100%">
                        <thead>
                          <tr>
                            <th>Posición</th>
                            <th>Universidad</th>
                            <th>Puntaje</th>
                          </tr>
                        </thead>
                        <tbody>
                          {/* {% for university in universities %} */}
                            <tr>
                              <td>1</td>
                              <td>[UNIVERSITY]</td>
                              <td>[TOTAL_SCORE]</td>
                            </tr>
                          {/* {% endfor %} */}
                        </tbody>
                      </table>
                    </div>
                  </div>
                  <div class="col-md-5">
                    <div class="row justify-content-between">
                      <h1 class="col-md-6">
                        Tabla Deporte
                      </h1>
                      <select id="sport-select" class="browser-default custom-select col-md-5 my-auto mr-3">
                        <option value="0" selected disabled>Escoger un Deporte</option>
                        {/* {% for sport in sports %} */}
                          <option value="{{ sport.id }}">
                            [SPORT]
                          </option>
                        {/* {% endfor %} */}
                      </select>
                    </div>
                    <div class="mt-4">
                      <table id="dt-deporte"
                            class="table table-striped table-bordered table-hover"
                            cellspacing="0"
                            width="100%">
                        <thead>
                          <tr>
                            <th>Posición</th>
                            <th>Universidad</th>
                            <th>Puntaje</th>
                          </tr>
                        </thead>
                        <tbody id="sport_score_table">
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
    );
  }
  