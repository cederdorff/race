# Opgaver og øvelser

Alle opgaver og øvelser på GitHub, ét forløb ad gangen. Hver række viser, hvor opgaveteksten ligger, og hvilke repos der hører til.

- **Opgave:** markdown-filen med opgaveteksten.
- **Starter:** det, de studerende starter fra. Typisk et GitHub-template ("Use this template").
- **Løsning:** færdig kode. Står der en branch, ligger løsningen på den branch.
- **Inline:** løsningsforslagene står i opgaveteksten som fold-ud-bokse.
- **—** betyder, at der ikke findes et repo til det.

*Opdateret 08-10-2026 ud fra opgavetekster, READMEs og branches i `cederdorff/*`. Den fulde liste over alle markdown-filer står i [markdown-filer.md](markdown-filer.md).*

**Forløb:** [WU-E26A](#wu-e26a--1-semester-webudvikling-efterår-2026) · [MDU-E25IXD](#mdu-e25ixd--3-semester-ixd-efterår-2026) · [Figma til React og gestures](#interactive-design-and-development-forår-2026) · [Supabase](#web-app--supabase-forår-2026) · [Movie App](#javascript-movie-app) · [Ældre forløb](#ældre-forløb-2024-2025) · [Guides](#guides) · [Repos efter rolle](#repos-efter-rolle)

---

## WU-E26A · 1. semester Webudvikling (efterår 2026)

Opgaverne ligger i [`wu-e26a/opgaver/`](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/README.md). Alle opgaver har løsningsforslag inline. De studerende starter fra en tom mappe, så der er ingen starter-repos.

### AMAbot-øvelser

Løsningerne ligger som `solve-…`-branches i [`node-express-ejs-client-server-app`](https://github.com/cederdorff/node-express-ejs-client-server-app).

| # | Opgave | Løsning |
| --- | --- | --- |
| 1 | [Din første server-renderede EJS-app](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-formular.md) | [`solve-1-express-ejs-formular`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-1-express-ejs-formular) |
| 2 | [Formhåndtering, validering og svarlogik](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-formhaandtering-svarlogik.md) | [`solve-2-express-ejs-formhaandtering-svarlogik`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-2-express-ejs-formhaandtering-svarlogik) |
| 3 | [Server-renderet AMAbot](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-amabot.md) | [`solve-3-express-ejs-amabot`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-3-express-ejs-amabot) |
| 4 | [Scoring og statistik](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-amabot-statistik.md) | [`solve-4-express-ejs-amabot-statistik`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-4-express-ejs-amabot-statistik) |
| 4+ | [JavaScript-øvelser til AMAbot](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/javascript-oevelser-amabot.md) | Inline |
| 5 | [Gem chathistorik i JSON](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-amabot-persistens.md) | [`solve-5-express-ejs-amabot-persistens`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-5-express-ejs-amabot-persistens) |
| 6 | [AMAbotten som REST API](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-amabot.md) | [`solve-6-express-rest-api-amabot`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-6-express-rest-api-amabot) |
| 7 | [Routes og data-modul](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-amabot-arkitektur.md) | [`solve-7-express-rest-api-amabot-arkitektur`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-7-express-rest-api-amabot-arkitektur) |
| 8 | [Frontend med fetch og DOM](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/fetch-dom-amabot.md) | [`solve-8-fetch-dom-amabot`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-8-fetch-dom-amabot) |
| 9 | [Sikkerhed og fejlhåndtering](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-amabot-sikkerhed-og-fejlhaandtering.md) | Kun inline (ingen branch endnu) |

### Students-opgaver

Løsningerne er beskrevet i README'en til [`express-rest-api-students`](https://github.com/cederdorff/express-rest-api-students#readme).

| Opgave | Før AMAbot | Løsning |
| --- | --- | --- |
| [JSON: Studerende i en JSON-fil](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-ejs-json-students.md) | 5 | [`express-ejs-json-students`](https://github.com/cederdorff/express-ejs-json-students) (`main`) |
| [REST API: Studerende med CRUD](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-students.md) | 6 | [`express-rest-api-students`](https://github.com/cederdorff/express-rest-api-students) (`main`) |
| [REST API: Arkitektur](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-arkitektur.md) | 7 | Branches i `express-rest-api-students`: [`routes-split`](https://github.com/cederdorff/express-rest-api-students/tree/routes-split) → [`data-module`](https://github.com/cederdorff/express-rest-api-students/tree/data-module) → [`filtering-sorting-pagination`](https://github.com/cederdorff/express-rest-api-students/tree/filtering-sorting-pagination) → [`layered-architecture-optional`](https://github.com/cederdorff/express-rest-api-students/tree/layered-architecture-optional) |
| [REST API: Fejlhåndtering](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-rest-api-fejlhaandtering.md) | 9 | [`error-handling`](https://github.com/cederdorff/express-rest-api-students/tree/error-handling) |

### Kom i gang med Node og Express

| Opgave | Løsning |
| --- | --- |
| [Hello Node.js](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/hello-node.md) | — |
| [Hello HTTP Module](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/hello-http-module.md) | [`hello-http-module`](https://github.com/cederdorff/hello-http-module) |
| [Hello Express.js](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/hello-express.md) | [`node-express-todos-rest-api`](https://github.com/cederdorff/node-express-todos-rest-api) |
| [Node.js File System](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/node-file-system.md) | — |
| [Express Users & Posts API](https://github.com/cederdorff/wu-e26a/blob/main/opgaver/express-users-posts-api.md) | — |

Demo-repo fra undervisningen: [`node-express-rest-todos`](https://github.com/cederdorff/node-express-rest-todos) (branch [`layered-architecture-demo`](https://github.com/cederdorff/node-express-rest-todos/tree/layered-architecture-demo)).

### React

| Opgave | Starter | Løsning |
| --- | --- | --- |
| RACE 8 · Thinking in React, øvelse 1–11. Ligger i [slides](https://cederdorff.com/wu-e26a/react-intro/#/ovelser), ikke som markdown | — | [`my-first-react-app`](https://github.com/cederdorff/my-first-react-app): én branch per øvelse (`ovelse-02-ret-og-gem` … `ovelse-10b-state`) |

---

## MDU-E25IXD · 3. semester IxD (efterår 2026)

Materialet ligger i [`mdu-e25ixd/undervisning/`](https://github.com/cederdorff/mdu-e25ixd/tree/main/undervisning). Case 1 i Product Optimization bygger på startprojektet [`mellemrum`](https://github.com/cederdorff/mellemrum). Til hver lektion er der eksempler og løsninger som branches i [`post-app-supabase`](https://github.com/cederdorff/post-app-supabase), som de studerende kender fra 2. semester.

### Product Optimization

| Lektion | Opgave / materiale | Starter | Løsning / eksempler |
| --- | --- | --- | --- |
| RACE 02 · [JavaScript for React](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/race-02-2026-08-21-javascript-for-react.md) | [JavaScript-koncepter til React](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/js-concepts.md) | — | — |
| RACE 03 · [Case 1 kick-off, fejlhåndtering og UI-states](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/race-03-2026-08-25-case-1-kick-off-fejlhaandtering-og-robuste-ui-states.md) | [Case 1 · Fra prototype til produktionsklar React-løsning](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/case-1-casebrief.md) | [`mellemrum`](https://github.com/cederdorff/mellemrum) (også branch `feature/mellemrum-case-starter`) | Ingen løsning (casen afleveres) |
| RACE 04 · [Arkitektur, styling og accessibility](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/race-04-2026-08-26-case-1-arkitektur-styling-og-accessibility.md) | Case 1 | `mellemrum` | Branches i `post-app-supabase`: [`refactor/architecture`](https://github.com/cederdorff/post-app-supabase/tree/refactor/architecture), [`refactor/react-styling`](https://github.com/cederdorff/post-app-supabase/tree/refactor/react-styling), [`refactor/react-a11y`](https://github.com/cederdorff/post-app-supabase/tree/refactor/react-a11y) |
| RACE 05 · [Datamodellering, relationer og Supabase](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/race-05-2026-09-01-case-1-datamodellering-relationer-og-supabase.md) | Case 1 | `mellemrum` | `post-app-supabase`: [`main`](https://github.com/cederdorff/post-app-supabase) (enkel `posts`-model), [`posts-with-duplicated-user-data`](https://github.com/cederdorff/post-app-supabase/tree/posts-with-duplicated-user-data), [`posts-and-users`](https://github.com/cederdorff/post-app-supabase/tree/posts-and-users) (relation) |
| RACE 06 · [Performance, Lighthouse og videre arbejde](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/race-06-2026-09-02-case-1-performance-lighthouse-og-videre-arbejde.md) | Case 1 | `mellemrum` | `post-app-supabase`: [`posts-and-users`](https://github.com/cederdorff/post-app-supabase/tree/posts-and-users), [`feature/select-post-user`](https://github.com/cederdorff/post-app-supabase/tree/feature/select-post-user), [`feature/performance-examples`](https://github.com/cederdorff/post-app-supabase/tree/feature/performance-examples) |
| RACE 07 · [Portfolio og faglig dokumentation](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/race-07-2026-10-12-portfolio-og-faglig-dokumentation.md) | Guide: [Hold dit Supabase-projekt i live med GitHub Actions](https://github.com/cederdorff/post-app-supabase/blob/main/docs/supabase-keep-alive.md). Skal sættes op i hvert repo med Supabase | — | — |
| Hele forløbet | [Teknisk audit-skabelon](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/teknisk-audit-skabelon.md) · [Eksamensbeskrivelse](https://github.com/cederdorff/mdu-e25ixd/blob/main/undervisning/product-optimization/eksamensbeskrivelse.md) | — | — |

### Dynamic User Interface

Lektionerne [RACE 08–18](https://github.com/cederdorff/mdu-e25ixd/tree/main/undervisning/dynamic-user-interface) (26-10 til 03-12) linker endnu ikke til opgaver eller repos.

---

## Interactive Design and Development (forår 2026)

Lektionerne ligger i [`figma-to-react/lessons/`](https://github.com/cederdorff/figma-to-react/blob/main/lessons.md).

| Opgave | Starter | Løsning |
| --- | --- | --- |
| [React Page Layout with Components](https://github.com/cederdorff/react-vite-page-layout/blob/main/docs/EXERCISE_GUIDE.md) | Ny Vite-app. Starterkoden står i guiden | [`react-vite-page-layout`](https://github.com/cederdorff/react-vite-page-layout) ([demo](https://cederdorff.com/react-vite-page-layout/)) |
| [Codeagram Feed with React Components](https://github.com/cederdorff/codeagram/blob/main/docs/EXERCISE_GUIDE.md) | Ny Vite-app. Starterkoden står i guiden | [`codeagram`](https://github.com/cederdorff/codeagram) (`main`). Udvidelser: branches `full-crud` og `motion-gestures` |
| Exercise 1 · [Hand Puck](https://github.com/cederdorff/webcam-ui/blob/main/README.md) | [`webcam-ui`](https://github.com/cederdorff/webcam-ui) (starterprojekt) | — |
| Exercise 2 · [Hand Catch Game](https://github.com/cederdorff/hand-catch-game/blob/main/README.md) | Bygger videre på `webcam-ui` | [`hand-catch-game`](https://github.com/cederdorff/hand-catch-game) og branch [`game-hand-catch`](https://github.com/cederdorff/webcam-ui/tree/game-hand-catch) i `webcam-ui` |
| Exercise 3 · [Air Juggler V1](https://github.com/cederdorff/air-juggler-game/blob/main/IMPLEMENTATION_GUIDE.md) | Bygger videre på `webcam-ui` | [`air-juggler-game`](https://github.com/cederdorff/air-juggler-game) |
| Showcase · [Air Juggler V2](https://github.com/cederdorff/webcam-controlled-game/blob/main/README.md) | [`webcam-controlled-game`](https://github.com/cederdorff/webcam-controlled-game) (GitHub-template) | — |
| Showcase · Dandelion Field | — | [`dandelion-experiment`](https://github.com/cederdorff/dandelion-experiment) |
| Guides: [Tool Setup](https://github.com/cederdorff/figma-to-react/blob/main/guides/tool-setup-guide.md), [Figma MCP](https://github.com/cederdorff/figma-to-react/blob/main/guides/figma-mcp-starter-guide.md), [Figma → Motion → MCP](https://github.com/cederdorff/figma-to-react/blob/main/guides/figma-motion-mcp-experiment-guide.md), [Motion for React](https://github.com/cederdorff/figma-to-react/blob/main/guides/motion-react-guided-tour.md), [Lottie](https://github.com/cederdorff/figma-to-react/blob/main/guides/lottie-figma-to-react-guide.md), [Haptics + Motion Lab](https://github.com/cederdorff/figma-to-react/blob/main/guides/haptics-gesture-exercise.md) | [`project-template`](https://github.com/cederdorff/project-template) (bruges i Tool Setup) | — |

---

## Web App · Supabase (forår 2026)

Lektioner og øvelser ligger i [`web-app-supabase`](https://github.com/cederdorff/web-app-supabase) (`_lessons/` og `_exercises/`).

| Opgave | Starter | Løsning |
| --- | --- | --- |
| RACE 8 · [Kom i gang med Supabase (Users)](https://github.com/cederdorff/react-supabase-users/blob/main/README.md) | — | [`react-supabase-users`](https://github.com/cederdorff/react-supabase-users) (også branch `react-router`) |
| RACE 9 · [Fra Thunder Client til React](https://github.com/cederdorff/web-app-supabase/blob/main/_exercises/race-9-oevelse-thunderclient-til-react.md) | [`react-supabase-products-template`](https://github.com/cederdorff/react-supabase-products-template) | [`react-supabase-products`](https://github.com/cederdorff/react-supabase-products) + inline |
| RACE 10 · [Post App med Forms og CRUD](https://github.com/cederdorff/web-app-supabase/blob/main/_exercises/race-10-oevelse-post-app-forms-and-crud.md) | [`post-app-supabase-template`](https://github.com/cederdorff/post-app-supabase-template) | [`post-app-supabase`](https://github.com/cederdorff/post-app-supabase) (`main`). Afsnit 9 · Ekstra udfordringer: branch [`opgave-9-udvidede-losninger`](https://github.com/cederdorff/post-app-supabase/tree/opgave-9-udvidede-losninger) |
| RACE 11 · [Filter, sort og samarbejde](https://github.com/cederdorff/web-app-supabase/blob/main/_lessons/race-11-filter-sort-collaboration.md) | [`react-router-spa`](https://github.com/cederdorff/react-router-spa) med guides til [GitHub Pages](https://github.com/cederdorff/react-router-spa/blob/main/docs/template-to-github-pages-setup.md) og [samarbejde](https://github.com/cederdorff/react-router-spa/blob/main/docs/collaboration-guide.md) | Branches i `post-app-supabase`: [`filter-server-side`](https://github.com/cederdorff/post-app-supabase/tree/filter-server-side) og [`filter-client-side`](https://github.com/cederdorff/post-app-supabase/tree/filter-client-side) |

Varianter: [`react-router-supabase`](https://github.com/cederdorff/react-router-supabase) er `react-router-spa` med Supabase-guides i `docs/`, og `react-router-spa` har også branchen `supabase-starter`. Opgaveteksten til RACE 10 står også i README'en til `post-app-supabase` og `post-app-supabase-template`.

---

## JavaScript Movie App

4-dages forløb for begyndere. Opgaverne ligger i [`js-movie-app/_exercises/`](https://github.com/cederdorff/js-movie-app/tree/main/_exercises).

| Opgave | Starter | Løsning |
| --- | --- | --- |
| [Dag 1 · JS basics og klik-tæller](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-1.md) | [`js-movie-app-template`](https://github.com/cederdorff/js-movie-app-template) | `js-movie-app/_solutions/dag1/` |
| [Dag 2 · Arrays, loops og film-lister](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-2.md) | Fortsætter | `_solutions/dag2/` |
| [Dag 2 ekstra · Personliste](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/personer-liste-ekstraopgave-dag2.md) | — | `_solutions/dag2-ekstra-personliste/` |
| [Dag 3 · Fetch, JSON og genre-filter](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-3.md) | Fortsætter | `_solutions/dag3/` |
| [Dag 4 · Søgning, sortering, dialog og GitHub Pages](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/movie-app-4.md) | Fortsætter | `_solutions/dag4/` og branch [`solution`](https://github.com/cederdorff/js-movie-app/tree/solution) |
| [Games App · kom godt i gang](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/games-app-guide.md) | — | — |
| [Emneoversigt](https://github.com/cederdorff/js-movie-app/blob/main/_exercises/emneoversigt.md) (hvilke emner hver dag dækker) | — | — |

`js-movie-app` har også branches med andre versioner af løsningen: [`part-2`](https://github.com/cederdorff/js-movie-app/tree/part-2), [`part-3`](https://github.com/cederdorff/js-movie-app/tree/part-3), [`simpel-filter-implementation`](https://github.com/cederdorff/js-movie-app/tree/simpel-filter-implementation), [`full-implementation`](https://github.com/cederdorff/js-movie-app/tree/full-implementation) og [`favorites`](https://github.com/cederdorff/js-movie-app/tree/favorites) (favoritter med localStorage).

[`movie-app`](https://github.com/cederdorff/movie-app) har samme filer som `js-movie-app-template` og er sandsynligvis en ældre kopi.

---

## Ældre forløb (2024–2025)

| Opgave | Starter | Løsning |
| --- | --- | --- |
| [React: Props, State, useEffect og komponenter](https://github.com/cederdorff/react-user-cards/blob/main/components-props-and-states.md) | — | Branches i [`react-user-cards`](https://github.com/cederdorff/react-user-cards): `1-props` → `2-likes-and-details` → … → `7-api-advanced` |
| [React CRUD App med Firebase REST](https://github.com/cederdorff/post-app-with-firebase/blob/main/_exercises/react-firebase-guide.md) | [`react-vite-spa`](https://github.com/cederdorff/react-vite-spa). Også [`post-app-with-firebase-template`](https://github.com/cederdorff/post-app-with-firebase-template) | [`post-app-with-firebase`](https://github.com/cederdorff/post-app-with-firebase): én branch per trin (`simple-version`, `loader`, `error-messages`, `image-upload`, `authentication`, `a11y` …) |
| [Next.js Post App](https://github.com/cederdorff/next-post-app-2025/blob/main/next-post-app.md) | [`next-post-app-2025`](https://github.com/cederdorff/next-post-app-2025) (GitHub-template) | — |
| [Migrer til Tailwind](https://github.com/cederdorff/next-post-app-2025/blob/main/tailwind-migration.md) | `next-post-app-2025` | Branch [`tailwind-migration`](https://github.com/cederdorff/next-post-app-2025/tree/tailwind-migration) |
| [Implementer TypeScript](https://github.com/cederdorff/next-post-app-2025/blob/main/typescript-migration.md) | `next-post-app-2025` | Branch [`typescript-migration`](https://github.com/cederdorff/next-post-app-2025/tree/typescript-migration) |
| [Opret React SPA med Vite og React Router](https://github.com/cederdorff/react-vite-spa/blob/main/react-router-spa.md) | — | [`react-vite-spa`](https://github.com/cederdorff/react-vite-spa) |
| [React SPA · deployment og samarbejde](https://github.com/cederdorff/react-vite-spa/blob/main/deployment-collaboration.md) | [`react-vite-spa`](https://github.com/cederdorff/react-vite-spa) | — |
| [Node Express Message REST API](https://github.com/cederdorff/node-express-message-rest-api/blob/main/node-express-message-rest-api.md) | — | [`node-express-message-rest-api`](https://github.com/cederdorff/node-express-message-rest-api) (`main`). Udvidelser som branches: `feature/chat-endpoints-exercises`, `feature/error-handling-statuscodes`, `feature/filter-sort-paginate`, `filter-search-query`, `feature/cors-examples`, `feature/jwt-auth`, `supabase` |
| Express og EJS 1 · [Simple Client-Server App](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/1_Building_a_Simple_Client_Server_App_with_Node_Express_EJS.md) | — | Branch [`solve-1_Building_a_Simple_Client_Server_App_with_Node_Express_EJS-md`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-1_Building_a_Simple_Client_Server_App_with_Node_Express_EJS-md) |
| Express og EJS 2 · [Formhåndtering og svarlogik](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/2_Form_haandtering_og_svar_logik.md) | — | Branch [`solve-2_Form_haandtering_og_svar_logik-md`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-2_Form_haandtering_og_svar_logik-md) |
| Express og EJS 3 · [Chatbot med Express og EJS](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/3_Chatbot_med_Express_og_EJS.md) | — | Branch [`solve-3_Chatbot_med_Express_og_EJS-md`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/solve-3_Chatbot_med_Express_og_EJS-md) |
| Express og EJS 4 · [Chatlogik med arrays og objekter](https://github.com/cederdorff/node-express-ejs-client-server-app/blob/main/_exercises/4_Chat_logik_med_arrays_objekter.md) | — | — |
| Portfolio · [username.github.io](https://github.com/cederdorff/username.github.io/blob/main/README.md) | [`username.github.io`](https://github.com/cederdorff/username.github.io) (GitHub-template) | — |

`post-app-test-frontend` er en kopi af `post-app-with-firebase`, og `web-app-race` er en kopi af `react-vite-spa`. `next-post-app-2025` har også løsnings-branches til `authjs-github-login` og `firebase-authentication`, men der er ingen opgavetekst til dem.

---

## Guides

Vejledninger, som flere forløb bruger. De er ikke opgaver.

| Guide | Ligger i |
| --- | --- |
| [Fra template til GitHub Pages](https://github.com/cederdorff/react-router-spa/blob/main/docs/template-to-github-pages-setup.md) | `react-router-spa` (kopi i `react-router-supabase`) |
| [GitHub Pages uden starter-template](https://github.com/cederdorff/react-router-spa/blob/main/docs/github-pages-setup-without-template.md) | `react-router-spa` |
| [Samarbejdsguide: Git, branches og Pull Requests](https://github.com/cederdorff/react-router-spa/blob/main/docs/collaboration-guide.md) | `react-router-spa` (kopi i `react-router-supabase`) |
| [Git og GitHub master-slides](https://github.com/cederdorff/react-router-spa/blob/main/docs/git-github-slides-master.md) og [speaker notes](https://github.com/cederdorff/react-router-spa/blob/main/docs/git-github-slides-master-speaker-notes.md) | `react-router-spa` (kopi i `react-router-supabase`) |
| [Tjekliste: GitHub Pages, React Router og Supabase](https://github.com/cederdorff/react-router-supabase/blob/main/docs/checklist-github-pages-supabase.md) | `react-router-supabase` |
| [Supabase setup til Posts](https://github.com/cederdorff/react-router-supabase/blob/main/docs/supabase-setup.md) | `react-router-supabase` |
| [Hold dit Supabase-projekt i live med GitHub Actions](https://github.com/cederdorff/post-app-supabase/blob/main/docs/supabase-keep-alive.md) | `post-app-supabase` |
| [Kom i gang med Supabase (Products)](https://github.com/cederdorff/web-app-supabase#readme) | README i `web-app-supabase` og `react-supabase-products(-template)` |

---

## Repos efter rolle

### Starter-templates

| Repo | Til |
| --- | --- |
| [`post-app-supabase-template`](https://github.com/cederdorff/post-app-supabase-template) | Supabase RACE 10 |
| [`react-supabase-products-template`](https://github.com/cederdorff/react-supabase-products-template) | Supabase RACE 9 |
| [`react-router-spa`](https://github.com/cederdorff/react-router-spa) / [`react-router-supabase`](https://github.com/cederdorff/react-router-supabase) | Supabase RACE 11, projekter |
| [`mellemrum`](https://github.com/cederdorff/mellemrum) | MDU Case 1 |
| [`webcam-ui`](https://github.com/cederdorff/webcam-ui) | Gesture-øvelser |
| [`webcam-controlled-game`](https://github.com/cederdorff/webcam-controlled-game) | Air Juggler V2 |
| [`js-movie-app-template`](https://github.com/cederdorff/js-movie-app-template) | Movie App |
| [`project-template`](https://github.com/cederdorff/project-template) | Vanilla JS-projekter |
| [`react-vite-spa`](https://github.com/cederdorff/react-vite-spa) | Firebase-opgaven, React SPA |
| [`post-app-with-firebase-template`](https://github.com/cederdorff/post-app-with-firebase-template) | Firebase-opgaven |
| [`next-post-app-2025`](https://github.com/cederdorff/next-post-app-2025) | Next.js-opgaverne |
| [`username.github.io`](https://github.com/cederdorff/username.github.io) | Portfolio |

### Løsninger

| Repo | Løser | Hvordan |
| --- | --- | --- |
| [`node-express-ejs-client-server-app`](https://github.com/cederdorff/node-express-ejs-client-server-app) | AMAbot 1–8 (WU-E26A) og ældre chatbot-øvelser | `solve-…`-branches |
| [`hello-http-module`](https://github.com/cederdorff/hello-http-module) | Hello HTTP Module (WU-E26A) | `main` |
| [`node-express-todos-rest-api`](https://github.com/cederdorff/node-express-todos-rest-api) | Hello Express (WU-E26A) | `main` |
| [`express-ejs-json-students`](https://github.com/cederdorff/express-ejs-json-students) | JSON-students | `main` |
| [`express-rest-api-students`](https://github.com/cederdorff/express-rest-api-students) | REST-, arkitektur- og fejlhåndterings-students | Én branch per del |
| [`my-first-react-app`](https://github.com/cederdorff/my-first-react-app) | RACE 8 · Thinking in React | Én branch per øvelse |
| [`react-supabase-products`](https://github.com/cederdorff/react-supabase-products) | Supabase RACE 9 | `main` |
| [`post-app-supabase`](https://github.com/cederdorff/post-app-supabase) | Supabase RACE 10–11 og eksempler til MDU Case 1 | `main` + mange branches |
| [`react-supabase-users`](https://github.com/cederdorff/react-supabase-users) | Supabase RACE 8 | `main` |
| [`js-movie-app`](https://github.com/cederdorff/js-movie-app) | Movie App dag 1–4 | `_solutions/` + branch `solution` |
| [`react-vite-page-layout`](https://github.com/cederdorff/react-vite-page-layout) | React Page Layout | `main` |
| [`codeagram`](https://github.com/cederdorff/codeagram) | Codeagram Feed | `main` + udvidelser |
| [`hand-catch-game`](https://github.com/cederdorff/hand-catch-game) | Hand Catch | `main` |
| [`air-juggler-game`](https://github.com/cederdorff/air-juggler-game) | Air Juggler V1 | `main` |
| [`react-user-cards`](https://github.com/cederdorff/react-user-cards) | Props, State og komponenter | Én branch per trin |
| [`post-app-with-firebase`](https://github.com/cederdorff/post-app-with-firebase) | React CRUD med Firebase | Én branch per trin |
| [`next-post-app-2025`](https://github.com/cederdorff/next-post-app-2025) | Tailwind og TypeScript | Branches |
| [`node-express-message-rest-api`](https://github.com/cederdorff/node-express-message-rest-api) | Message REST API | `main` + udvidelser som branches |

### Andre branches uden opgavetekst

Disse branches er ikke linket fra nogen opgave eller lektion. De er eksempler fra undervisningen eller ekstra løsninger.

| Repo | Branch | Indhold |
| --- | --- | --- |
| `post-app-supabase` | [`error-messages-and-loading-states`](https://github.com/cederdorff/post-app-supabase/tree/error-messages-and-loading-states), [`error-handling-and-ui-states`](https://github.com/cederdorff/post-app-supabase/tree/error-handling-and-ui-states), [`performative-ui`](https://github.com/cederdorff/post-app-supabase/tree/performative-ui) | Fejlhåndtering, loading-states og UI-eksempler (relateret til afsnit 9 i RACE 10) |
| `express-rest-api-students` | [`data-helpers-import-export`](https://github.com/cederdorff/express-rest-api-students/tree/data-helpers-import-export) | Variant af data-modulet |
| `node-express-ejs-client-server-app` | [`split-client-server`](https://github.com/cederdorff/node-express-ejs-client-server-app/tree/split-client-server) | Client/server-opdeling (2025, før AMAbot-øvelse 6) |
| `hello-http-module` | [`get-request-data`](https://github.com/cederdorff/hello-http-module/tree/get-request-data) | Læs request-data (2023) |
| `next-post-app-2025` | [`tailwind-ui-component-example`](https://github.com/cederdorff/next-post-app-2025/tree/tailwind-ui-component-example), [`authjs-github-login`](https://github.com/cederdorff/next-post-app-2025/tree/authjs-github-login), [`firebase-authentication`](https://github.com/cederdorff/next-post-app-2025/tree/firebase-authentication) | Tailwind-komponenter og login |
| `react-router-spa` | [`feature/fetch-products-from-json-file`](https://github.com/cederdorff/react-router-spa/tree/feature/fetch-products-from-json-file), [`supabase-starter`](https://github.com/cederdorff/react-router-spa/tree/supabase-starter) | Hent produkter fra JSON-fil, Supabase-starter |
| `react-vite-spa` | [`component-styles`](https://github.com/cederdorff/react-vite-spa/tree/component-styles), [`component-styles-modules`](https://github.com/cederdorff/react-vite-spa/tree/component-styles-modules) | Styling af komponenter (CSS og CSS Modules) |
| `project-template` | [`hello-js`](https://github.com/cederdorff/project-template/tree/hello-js), [`new-project-template`](https://github.com/cederdorff/project-template/tree/new-project-template) | Varianter af vanilla-starteren |

### Kopier, som kan slettes eller arkiveres

| Kopi | Original |
| --- | --- |
| `post-app-test-frontend` | `post-app-with-firebase` |
| `web-app-race` | `react-vite-spa` |
| `movie-app` | `js-movie-app-template` |
| `_lessons/` i `react-supabase-products` | `_lessons/` i `web-app-supabase` |
| `_exercises/express-ejs-json-students.md` i `express-ejs-json-students` | `wu-e26a/opgaver/express-ejs-json-students.md` |
| `docs/` i `react-router-supabase` (delvist) | `docs/` i `react-router-spa` |
