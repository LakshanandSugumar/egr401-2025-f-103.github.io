# Team 20 · Solar Tracker Tilt-Sensing System

Project website for Team 20 (EGR 401/402 Senior Capstone, ASU Polytechnic), sponsored by ARRAY Technologies.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Pages live in `docs/`, navigation in `mkdocs.yml`.
Every push to `main` builds the site and deploys it to the `gh-pages` branch through `.github/workflows/main.yml`.

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve
```

## Camera concept simulation

- `docs/camera-concept/sim/index.html`: in-browser 3D field simulation (Three.js), served at `/camera-concept/sim/`
- `simulation/gazebo/`: the same setup as a Gazebo Harmonic world, with teach/test scripts. See the Gazebo Model page on the site.
