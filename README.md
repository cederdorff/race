# RACE · Oversigt over repositories

Overblik over Rasmus Cederdorffs (RACE) repositories til undervisning, opgaver og øvelser på EAAA. Oversigten viser, hvor markdown-opgaverne ligger, og hvad hvert repo bruges til.

*Opdateret 07-10-2026. Oversigten er lavet ved at scanne alle `cederdorff/*`-repos for markdown-filer.*

> **Alle markdown-filer:** [`markdown-filer.md`](markdown-filer.md) er en komplet liste over alle `.md`-filer i dine repos med links og titler. Den genereres med `python3 scripts/generate-markdown-index.py` (henter repo-listen fra GitHub og kloner overfladisk). Denne README er den håndskrevne oversigt over kurser og opgaver.

**Hurtige genveje**

- 1. semester Webudvikling (WU-E26A): [alle opgaver](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/README.md) · [forløb og lektioner](https://github.com/cederdorff/wu-e26a#readme) · [slides](https://cederdorff.com/wu-e26a/)
- 3. semester IxD (MDU-E25IXD): [forløb og lektioner](https://github.com/cederdorff/mdu-e25ixd#readme) · [Case 1](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/case-1-casebrief.md)
- Dette repo: [fælles data, billeder og slides](#dette-repo-race)

---

## Sådan er materialet organiseret

Opgaver og øvelser ligger efter tre mønstre:

| Mønster | Hvor | Eksempler |
| --- | --- | --- |
| **Kursus-repo** (nyeste, 2026) | Ét repo per hold med `undervisning/`, `opgaver/` og slides | `wu-e26a`, `mdu-e25ixd`, `figma-to-react` |
| **Øvelses-repo med `_exercises/` og `_lessons/`** (2025–forår 2026) | Opgavetekster ligger i samme repo som starterkode eller løsning | `js-movie-app`, `web-app-supabase`, `node-express-ejs-client-server-app` |
| **Opgaven er README'en** | Hele opgaveteksten står i `README.md` | `post-app-supabase`, `react-supabase-products`, `react-supabase-users` |

Opgavetekster ligger nogle gange to steder. Øvelserne i `react-supabase-products` findes også i `web-app-supabase`, og guiderne i `react-vite-spa` og `web-app-race` er ens.

---

## 1. Aktive kursus-repos (efterår 2026)

### WU-E26A · 1. semester Webudvikling → [`cederdorff/wu-e26a`](https://github.com/cederdorff/wu-e26a)

Spejl af Canvas-kurset med undervisningsplaner, forberedelse, slides og opgaver. Forløb: **AMAbot** (uge 35–40), **Chatbot** (uge 41–46) og **Semesterprojekt** (uge 47–51).

| Mappe | Indhold |
| --- | --- |
| [`opgaver/`](https://github.com/cederdorff/wu-e26a/tree/main/opgaver) | Alle opgaver i rækkefølge, se [opgaver/README.md](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/README.md) |
| [`undervisning/`](https://github.com/cederdorff/wu-e26a/tree/main/undervisning) | En markdown-fil per Canvas-modul (001–0xx), plus `_skabelon.md` |
| [`canvas/`](https://github.com/cederdorff/wu-e26a/tree/main/canvas) | Modulnavne til Canvas |
| [`materialer/`](https://github.com/cederdorff/wu-e26a/tree/main/materialer) | Fælles materialer |

**Opgaver i `wu-e26a/opgaver/`**

| Spor | Opgave |
| --- | --- |
| Kom i gang | [Hello Node.js](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/hello-node.md) · [Hello HTTP Module](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/hello-http-module.md) · [Hello Express.js](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/hello-express.md) · [Node.js File System](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/node-file-system.md) · [Express Users & Posts API](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-users-posts-api.md) |
| AMAbot 1 | [Din første server-renderede EJS-app](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-formular.md) |
| AMAbot 2 | [Formhåndtering, validering og svarlogik](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-formhaandtering-svarlogik.md) |
| AMAbot 3 | [Server-renderet AMAbot med regelbaseret svarlogik](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-amabot.md) |
| AMAbot 4 | [Scoring og statistik](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-amabot-statistik.md) (+ [JavaScript-øvelser til AMAbot](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/javascript-oevelser-amabot.md)) |
| AMAbot 5 | [Gem chathistorik i en JSON-fil](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-amabot-persistens.md) |
| AMAbot 6 | [AMAbotten som REST API](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-amabot.md) |
| AMAbot 7 | [Routes og data-modul](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-amabot-arkitektur.md) |
| AMAbot 8 | [Frontend med fetch og DOM](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/fetch-dom-amabot.md) |
| AMAbot 9 | [Sikkerhed og fejlhåndtering](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-amabot-sikkerhed-og-fejlhaandtering.md) |
| Students | [JSON-filer](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-json-students.md) · [REST CRUD](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-students.md) · [Arkitektur](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-arkitektur.md) · [Fejlhåndtering](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-fejlhaandtering.md) |
| React (RACE 8) | Øvelse 1–11 ligger i slides: [cederdorff.com/wu-e26a/react-intro/#/ovelser](https://cederdorff.com/wu-e26a/react-intro/#/ovelser) |

**Løsningsforslag og demo-repos til WU-E26A**

| Repo | Hører til |
| --- | --- |
| [`express-ejs-json-students`](https://github.com/cederdorff/express-ejs-json-students) | Løsning til JSON-students. Har også en kopi af opgaven i `_exercises/` |
| [`express-rest-api-students`](https://github.com/cederdorff/express-rest-api-students) | Løsning til students-opgaverne om REST API |
| [`node-express-rest-todos`](https://github.com/cederdorff/node-express-rest-todos) | Demo: REST API med todos |
| [`node-express-ejs-client-server-app`](https://github.com/cederdorff/node-express-ejs-client-server-app) | Demo og ældre øvelser 1–4 om Express, EJS og chatbot i `_exercises/` (se afsnit 3) |
| [`my-first-react-app`](https://github.com/cederdorff/my-first-react-app) | Løsning til RACE 8 · Thinking in React |

### MDU-E25IXD · 3. semester Interaction Design → [`cederdorff/mdu-e25ixd`](https://github.com/cederdorff/mdu-e25ixd)

Materialeoversigt for **Product Optimization** og **Dynamic User Interface**. `race-*.md`-filerne synkroniseres automatisk til Canvas med GitHub Actions.

| Mappe / fil | Indhold |
| --- | --- |
| [`undervisning/semesterstart/`](https://github.com/cederdorff/mdu-e25ixd/tree/main/undervisning/semesterstart) | Semesterstart og portfolio-feedback |
| [`undervisning/product-optimization/`](https://github.com/cederdorff/mdu-e25ixd/tree/main/undervisning/product-optimization) | Lektioner race-01 til race-07 plus forløbsmaterialer |
| [`undervisning/dynamic-user-interface/`](https://github.com/cederdorff/mdu-e25ixd/tree/main/undervisning/dynamic-user-interface) | Lektioner race-08 til race-18 (26-10 til 03-12) |
| [`semesteroverblik/`](https://github.com/cederdorff/mdu-e25ixd/tree/main/semesteroverblik) | Forløb og eksamener, Canvas-moduler, planlægningsnoter |
| `slides/` | Slides (publiceret på [cederdorff.com/mdu-e25ixd](https://cederdorff.com/mdu-e25ixd/)) |

**Opgaver og casemateriale**

- [Case 1 · Fra prototype til produktionsklar React-løsning](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/case-1-casebrief.md). Starterprojekt: [`cederdorff/mellemrum`](https://github.com/cederdorff/mellemrum)
- [Teknisk audit-skabelon](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/teknisk-audit-skabelon.md)
- [Eksamensbeskrivelse · Product Optimization](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/eksamensbeskrivelse.md)
- [JavaScript for React (koncepter)](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/js-concepts.md)

---

## 2. Kursus-repos fra foråret 2026

### Interactive Design and Development (maj–juni 2026) → [`cederdorff/figma-to-react`](https://github.com/cederdorff/figma-to-react)

Forløb om Figma til React og Gesture & Motion Design. Indeks: [`lessons.md`](https://github.com/cederdorff/figma-to-react/blob/main/lessons.md).

| Mappe | Indhold |
| --- | --- |
| [`lessons/`](https://github.com/cederdorff/figma-to-react/tree/main/lessons) | 17 lektionsplaner (04-05-2026 til 09-06-2026) og `overview.md` |
| [`guides/`](https://github.com/cederdorff/figma-to-react/tree/main/guides) | [Tool Setup](https://github.com/cederdorff/figma-to-react/blob/main/guides/tool-setup-guide.md) · [Figma MCP Starter](https://github.com/cederdorff/figma-to-react/blob/main/guides/figma-mcp-starter-guide.md) · [Figma → Motion → MCP](https://github.com/cederdorff/figma-to-react/blob/main/guides/figma-motion-mcp-experiment-guide.md) · [Motion for React](https://github.com/cederdorff/figma-to-react/blob/main/guides/motion-react-guided-tour.md) · [Lottie](https://github.com/cederdorff/figma-to-react/blob/main/guides/lottie-figma-to-react-guide.md) · [Haptics + Motion Lab](https://github.com/cederdorff/figma-to-react/blob/main/guides/haptics-gesture-exercise.md) |

**Webcam- og gesture-spil til samme forløb** (opgaven eller guiden står i README):

- [`webcam-controlled-game`](https://github.com/cederdorff/webcam-controlled-game): Air Juggler Student Guide (React + TensorFlow.js)
- [`air-juggler-game`](https://github.com/cederdorff/air-juggler-game): færdigt spil og [`IMPLEMENTATION_GUIDE.md`](https://github.com/cederdorff/air-juggler-game/blob/main/IMPLEMENTATION_GUIDE.md)
- [`hand-catch-game`](https://github.com/cederdorff/hand-catch-game): Hand Catch (MediaPipe)
- [`webcam-ui`](https://github.com/cederdorff/webcam-ui): Hand Puck
- [`dandelion-experiment`](https://github.com/cederdorff/dandelion-experiment): Dandelion Field (MediaPipe-eksperiment)

### Web App · Supabase-forløbet (RACE 8–11, april–maj 2026) → [`cederdorff/web-app-supabase`](https://github.com/cederdorff/web-app-supabase)

| Type | Filer |
| --- | --- |
| Lektioner (`_lessons/`) | [RACE 8 · Intro til Supabase](https://github.com/cederdorff/web-app-supabase/blob/main/_lessons/race-8-intro-to-supabase.md) · [RACE 9 · HTTP & REST API](https://github.com/cederdorff/web-app-supabase/blob/main/_lessons/race-9-http-and-rest-api.md) · [RACE 10 · Forms & CRUD](https://github.com/cederdorff/web-app-supabase/blob/main/_lessons/race-10-forms-and-crud.md) · [RACE 11 · Filter, sort og samarbejde](https://github.com/cederdorff/web-app-supabase/blob/main/_lessons/race-11-filter-sort-collaboration.md) |
| Øvelser (`_exercises/`) | [RACE 9 · Fra Thunder Client til React](https://github.com/cederdorff/web-app-supabase/blob/main/_exercises/race-9-oevelse-thunderclient-til-react.md) · [RACE 10 · Post App med Forms og CRUD](https://github.com/cederdorff/web-app-supabase/blob/main/_exercises/race-10-oevelse-post-app-forms-and-crud.md) |
| Supabase-guide | [README](https://github.com/cederdorff/web-app-supabase#readme): Kom i gang med Supabase |

Relaterede repos:

- [`react-supabase-products`](https://github.com/cederdorff/react-supabase-products) og [`react-supabase-products-template`](https://github.com/cederdorff/react-supabase-products-template): samme guide og lektioner (dublet)
- [`react-supabase-users`](https://github.com/cederdorff/react-supabase-users): Supabase-guide med users
- [`post-app-supabase`](https://github.com/cederdorff/post-app-supabase) og [`post-app-supabase-template`](https://github.com/cederdorff/post-app-supabase-template): **RACE 10-øvelsen står i README** (løsning og template). Plus [guide til Supabase keep-alive](https://github.com/cederdorff/post-app-supabase/blob/main/docs/supabase-keep-alive.md)
- [`react-router-supabase`](https://github.com/cederdorff/react-router-supabase): template med guides i `docs/` ([GitHub Pages + Supabase-tjekliste](https://github.com/cederdorff/react-router-supabase/blob/main/docs/checklist-github-pages-supabase.md), [Supabase-setup](https://github.com/cederdorff/react-router-supabase/blob/main/docs/supabase-setup.md), [samarbejdsguide](https://github.com/cederdorff/react-router-supabase/blob/main/docs/collaboration-guide.md), [Git/GitHub-slides](https://github.com/cederdorff/react-router-supabase/blob/main/docs/git-github-slides-master.md))

### JavaScript Movie App (4-dages forløb, multimediedesign) → [`cederdorff/js-movie-app`](https://github.com/cederdorff/js-movie-app)

| Type | Filer |
| --- | --- |
| Lektioner (`_lessons/`) | [Dag 1](https://github.com/cederdorff/js-movie-app/blob/main/_lessons/lektionsplan-dag1.md) · [Dag 2](https://github.com/cederdorff/js-movie-app/blob/main/_lessons/lektionsplan-dag2.md) · [Dag 3](https://github.com/cederdorff/js-movie-app/blob/main/_lessons/lektionsplan-dag3.md) · [Dag 4](https://github.com/cederdorff/js-movie-app/blob/main/_lessons/lektionsplan-dag4.md) |
| Øvelser (`_exercises/`) | [Movie App 1 · JS Basics](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-1.md) · [2 · Arrays & loops](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-2.md) · [3 · Fetch & JSON](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-3.md) · [4 · Søgning, sortering & GitHub Pages](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-4.md) · [Ekstra: Personliste](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/personer-liste-ekstraopgave-dag2.md) · [Games App-guide](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/games-app-guide.md) · [Emneoversigt](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/emneoversigt.md) |

Starter: [`js-movie-app-template`](https://github.com/cederdorff/js-movie-app-template).

### React-intro og komponentøvelser

| Repo | Opgave |
| --- | --- |
| [`react-vite-page-layout`](https://github.com/cederdorff/react-vite-page-layout) | [React Page Layout with Components](https://github.com/cederdorff/react-vite-page-layout/blob/main/docs/EXERCISE_GUIDE.md) |
| [`codeagram`](https://github.com/cederdorff/codeagram) | [Codeagram Feed with React Components](https://github.com/cederdorff/codeagram/blob/main/docs/EXERCISE_GUIDE.md) |
| [`react-user-cards`](https://github.com/cederdorff/react-user-cards) | [Props, State, useState, useEffect & komponenter](https://github.com/cederdorff/react-user-cards/blob/main/components-props-and-states.md) |
| [`react-router-spa`](https://github.com/cederdorff/react-router-spa) | Template med guides: [Template → GitHub Pages](https://github.com/cederdorff/react-router-spa/blob/main/docs/template-to-github-pages-setup.md) · [GitHub Pages uden template](https://github.com/cederdorff/react-router-spa/blob/main/docs/github-pages-setup-without-template.md) · [Samarbejdsguide](https://github.com/cederdorff/react-router-spa/blob/main/docs/collaboration-guide.md) |
| [`react-web-app`](https://github.com/cederdorff/react-web-app) | React Router SPA-template (engelsk README) |

---

## 3. Efterår 2025 og ældre øvelser med markdown

| Repo | Opgaver / guides |
| --- | --- |
| [`node-express-ejs-client-server-app`](https://github.com/cederdorff/node-express-ejs-client-server-app) | `_exercises/`: [1 · Client-Server App](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/1_Building_a_Simple_Client_Server_App_with_Node_Express_EJS.md) · [2 · Formhåndtering og svarlogik](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/2_Form_haandtering_og_svar_logik.md) · [3 · Chatbot med Express og EJS](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/3_Chatbot_med_Express_og_EJS.md) · [4 · Chatlogik med arrays & objekter](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/4_Chat_logik_med_arrays_objekter.md) |
| [`next-post-app-2025`](https://github.com/cederdorff/next-post-app-2025) | [Next.js Post App](https://github.com/cederdorff/next-post-app-2025/blob/main/next-post-app.md) · [Migrer til Tailwind](https://github.com/cederdorff/next-post-app-2025/blob/main/tailwind-migration.md) · [Implementer TypeScript](https://github.com/cederdorff/next-post-app-2025/blob/main/typescript-migration.md) |
| [`react-vite-spa`](https://github.com/cederdorff/react-vite-spa) / [`web-app-race`](https://github.com/cederdorff/web-app-race) | [Opret React SPA med Vite og React Router](https://github.com/cederdorff/react-vite-spa/blob/main/react-router-spa.md) · [Deployment & samarbejde](https://github.com/cederdorff/react-vite-spa/blob/main/deployment-collaboration.md) (ens filer i begge repos) |
| [`post-app-with-firebase`](https://github.com/cederdorff/post-app-with-firebase) / [`post-app-test-frontend`](https://github.com/cederdorff/post-app-test-frontend) | [React CRUD App with Firebase REST](https://github.com/cederdorff/post-app-with-firebase/blob/main/_exercises/react-firebase-guide.md) (ens filer i begge repos). Starter: [`post-app-with-firebase-template`](https://github.com/cederdorff/post-app-with-firebase-template) |
| [`chatbot`](https://github.com/cederdorff/chatbot) | AI Chatbot med Node-backend (README) |
| [`username.github.io`](https://github.com/cederdorff/username.github.io) | Portfolio-template til studerende. Guiden står i README |
| [`react-starters`](https://github.com/cederdorff/react-starters) | 16 små React-starters, hver med egen README (counter, forms, contact card, Firebase m.fl.) |
| [`ci-intro`](https://github.com/cederdorff/ci-intro) | GitHub Classroom-opgaver om Continuous Integration (README) |
| [`dat-js-exam-spring-2023`](https://github.com/cederdorff/dat-js-exam-spring-2023) | 1. semester-eksamen DAT23V1/V2 (README) |

---

## 4. Demo-, starter- og løsningsrepos uden opgavetekst

Disse repos har ingen opgavetekst, kun en standard-README eller ingen README. De bruges som kodedemo, starter eller løsning.

- **Node/Express:** `node-express-rest-users`, `node-express-users-mvc`, `node-express-todos-rest-api`, `node-express-message-rest-api`, `node-express-typescript`, `node-mysql`, `node-contacts`, `node-sequelize`, `hello-http-module`, `node-vanilla-todos-rest-api`, `node-vanilla-users-rest-api`, `musicbase-backend`, `musicbase-mongodb`
- **React/Vite:** `react-products`, `react-my-first-project`, `react-image-slider`, `react-user-crud-local-storage`, `react-vite-user-list`, `react-open-street-map`, `react-vite-*` (todo, later-list, mui, contacts, photo-app, crud-app, firebase-hosting, list-render, starter), `race-your-react-dev`, `webshop-products`, `portfolio-projects`
- **Next.js / Remix / React Router:** `next-post-app`, `next-my-first-project`, `next-auth-js`, `next-post-app-wp-rest`, `next-js-github-pages`, `remix-*` (post-app, auth-github/google/microsoft, pwa, photo-app, contacts, routing), `react-router-post-app`, `react-router-address-book`
- **Vanilla JS-starters:** `project-template`, `movie-picker`, `snap-scroll`, `ixd-studietur`, `fetch-teachers`, `fetch-teachers-wp`, `fetch-wp-posts`, `async-js-fetch-users`, `draggable-image-slider`, `simple-pwa`, `movie-app`
- **Mobil (Expo/Ionic):** `expo-post-app`, `expo-firebase`, `expo-tabs`, `react-native-expo-sticker-smash`, `web-mobile-app-dev`
- **Projekter og cases:** `mellemrum` (Case 1, 3. semester), `easy-tv`, `karolineshus`, `strapi-cloud-template-blog-*`
- **Ældre (2022–2023):** `dat-js`, `dat-js-crud-intro`, `js-user-crud`, `post-app`, `post-app-template`, `rest-*-crud-*`, `react-user-crud*`, `simple-*`, `web-frontend`, `mdu-frontend`, `it-architecture`, `slides` m.fl.

Se [`markdown-filer.md`](markdown-filer.md) for den fulde liste.

---

## 5. Studerendes repos og GitHub Classroom

Organisationerne `eaaa-dob-wu-e25a`, `eaaa-dob-wu-e24a` og `eaaa-dob-wu-e23a` indeholder studerendes afleveringer og gruppeprojekter, mest forks fra GitHub Classroom (fx `todo-list-*`, `counter-example-js-*`, `sign-up-page-*`, `recipebook-*`). Opgave-templates fra MAGL hedder `eaaa-magl-pro1-e25y-*`. Repoerne indeholder ingen af dine opgavetekster og er derfor ikke med i oversigten ovenfor.

---

## Dette repo (race)

Dette repo er et fælles lager for materialer, som andre repos, øvelser og slides henter direkte:

| Mappe | Indhold |
| --- | --- |
| [`data/`](data) | JSON-testdata til øvelser: `users.json`, `posts*.json`, `movies.json`, `games.json`, `expo-*.json`, `schoolSystem.json`, `todosUsersObject.json`, `webshop/` m.fl. |
| [`images/`](images) | Billeder til øvelser og slides (fx `ui-to-components.png`, `component-tree.avif`, `games/`, `users/`) |
| [`slides/`](slides) | PDF-slides: React, Node/Express, REST, Supabase, Firebase, auth, Git/GitHub, hackathons, studiepraktik m.m. |
| [`pdfs/`](pdfs), [`videos/`](videos), [`reels/`](reels) | Øvrige filer og videoer |
| [`scripts/`](scripts) | `generate-markdown-index.py`, som laver [`markdown-filer.md`](markdown-filer.md) |

---

## Forslag til mere overblik

1. **Én kilde per opgave.** Flere opgaver findes i to repos: `react-supabase-products` og `web-app-supabase`, `react-vite-spa` og `web-app-race`, `post-app-with-firebase` og `post-app-test-frontend`. Behold opgaveteksten ét sted og link til den fra de andre.
2. **Brug samme struktur fremover.** `wu-e26a` og `mdu-e25ixd` bruger `undervisning/` og `opgaver/` og har en README som indeks. Øvelses-repos kan nøjes med starterkode og et link tilbage til kursus-repoet.
3. **Arkivér gamle repos.** Repos fra 2022–2023 kan arkiveres på GitHub, så de ikke fylder i listen.
4. **Brug GitHub topics** (fx `wu-e26a`, `mdu-e25ixd`, `exercise`, `solution`, `template`), så du kan filtrere på github.com/cederdorff.
