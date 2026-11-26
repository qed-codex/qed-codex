---
{
  "module": "src/Development/WeilBound/CoreStatements/HeckeCharacterDeRham/DeRhamHeckeResults/LAdicHeckeDeRham/LAdicHeckeFields/FieldOfLeaves.lean",
  "declarations": [
    "PositivityTheory.SecR.Hladr2.hasPeriods_main"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Periods for the source’s local formal-group characters

[Theorem PHT.0083](https://andrewodesky.com/rh/lean/PositivityTheory.SecR.Hladr2.hasPeriods_main/)

Let $\ell$ be prime and let $G_{\mathbb Q_\ell}=\operatorname{Gal}(\overline{\mathbb Q}_\ell/\mathbb Q_\ell)$. Fix commutative rings $B,D$ with Galois actions, a filtration $\operatorname{Fil}^aD$ indexed by $a\in\mathbb Z$, and integral and comparison data satisfying the local ring, integral and comparison hypotheses below. Assume also the two universal hypotheses on tilt lifting and nonvanishing below.

Let $K\subseteq\overline{\mathbb Q}_\ell$ be finite over $\mathbb Q_\ell$, put $G_K=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K)$, and let $\chi:G_K\to K^\times$ be a group homomorphism continuous as a map to $\overline{\mathbb Q}_\ell$. Suppose there are a uniformizer $\pi\in\mathcal O_K$ and $z_n\in\overline{\mathbb Q}_\ell$ such that, with $q=|\mathcal O_K/(\pi)|$, $$z_0=0,\qquad z_1\ne0,\qquad z_{n+1}^q+\pi z_{n+1}=z_n\quad(n\ge0).$$ Put $f_\pi(T)=\pi T+T^q$. For every $g\in G_K$ and $\phi(T)=\sum_{i\ge0}\phi_iT^i\in\mathcal O_K[[T]]$ with $$\phi_0=0,\qquad \phi_1=\chi(g),\qquad \phi\circ f_\pi=f_\pi\circ\phi,$$ require convergence with the specified value $$\sum_{i\ge0}\phi_i z_n^i=g(z_n)\quad(n\ge0).$$ Call these the torsion conditions on $(K,\chi,\pi,z)$.

For every $\mathbb Q_\ell$-embedding $\mu:K\hookrightarrow\overline{\mathbb Q}_\ell$, there is $y\in D$ such that $$g(y)=\mu(\chi(g))y\quad\text{for all }g\in G_K\text{ fixing }\mu(K)\text{ pointwise}.$$ The scalar on the right uses the specified $\overline{\mathbb Q}_\ell$-algebra structure of $D$. If $\mu$ is the given inclusion of $K$, then $$y\in\operatorname{Fil}^1D\setminus\operatorname{Fil}^2D;$$ for every other $\mu$, $$y\in\operatorname{Fil}^0D\setminus\operatorname{Fil}^1D.$$
