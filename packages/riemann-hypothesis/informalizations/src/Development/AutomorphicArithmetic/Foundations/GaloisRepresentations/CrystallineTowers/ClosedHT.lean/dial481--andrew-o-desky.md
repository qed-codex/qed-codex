---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/ClosedHT.lean",
  "declarations": [
    "UpperTheory.Gal.Seam.HT.htBij"
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

## A functorial Hodge–Tate comparison for smooth projective models

[Theorem PHT.0030](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Seam.HT.htBij/)

Let $\ell$ be a prime, let $(\zeta_k)_{k\ge0}$ be the system of roots of unity of $\ell$-power order chosen in the introduction, and let $K\subset\overline{\mathbb Q}_\ell$ be a finite extension of $\mathbb Q_\ell$. For a scheme $\mathcal X$ over $\mathcal O_K$ write $X=\mathcal X_K$ for its generic fibre, $T^n(X)$ and $V^n(X)$ for the $\ell$-adic étale cohomology groups of the introduction, and $H^n_a(X/K)$ for the groups of ([Graded infinitesimal cohomology](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.HT.Hdg/)). There are maps $$h^{a,n}_{\mathcal X}:V^n(X)\times H^n_a(X/K)^*\longrightarrow\mathbb C_\ell,$$ one for every scheme $\mathcal X$ over $\mathcal O_K$ and all integers $a,n\ge0$, each $\mathbb Q_\ell$-linear in the first variable and $K$-linear in the second, such that the following nine assertions hold for every scheme $\mathcal X$ over $\mathcal O_K$ that is projective over $\mathcal O_K$, smooth over $\mathcal O_K$, and strictly semistable for some uniformizer of $\mathcal O_K$. The maps $\eta^{a,n}_{\mathcal X}$ and $\kappa^n_{\mathcal X}$ in assertions 4 and 7 to 9 are those that the introduction attaches to the maps $h^{a,n}_{\mathcal X}$ once assertion 1 holds.

1. Finiteness. For all integers $a,n\ge0$, the $K$-vector space $H^n_a(X/K)$ is finite-dimensional, and it is zero if $a>n$.
2. Galois action. For all integers $a,n\ge0$ and all $\gamma\in G_K$, $v\in V^n(X)$ and $\varphi\in H^n_a(X/K)^*$, $$\chi_\ell(\gamma)^a\,h^{a,n}_{\mathcal X}(\gamma v,\varphi)=\gamma\bigl(h^{a,n}_{\mathcal X}(v,\varphi)\bigr).$$
3. Naturality. Let $\mathcal Z$ be a second scheme over $\mathcal O_K$ that is projective over $\mathcal O_K$, smooth over $\mathcal O_K$, and strictly semistable for some uniformizer of $\mathcal O_K$, let $Z$ be its generic fibre, and let $g:\mathcal X\to\mathcal Z$ be a morphism over $\mathcal O_K$. For all integers $a,n\ge0$ and all $v\in V^n(Z)$ and $\varphi\in H^n_a(X/K)^*$, $$h^{a,n}_{\mathcal X}(g^*v,\varphi)=h^{a,n}_{\mathcal Z}(v,\varphi\circ g^*),$$ where $g^*:V^n(Z)\to V^n(X)$ and $g^*:H^n_a(Z/K)\to H^n_a(X/K)$ are the pullbacks along the morphism $g_K:X\to Z$ of generic fibres.
4. Cup products. Let $i,j\ge0$, and let $x\in T^i(X)$, $y\in T^j(X)$ and $z\in T^{i+j}(X)$ satisfy $z_k=x_k\cup y_k$ for every $k\ge0$. Then for every integer $a\ge0$, $$\eta^{a,i+j}_{\mathcal X}(z)=\sum_{a'+a''=a}\eta^{a',i}_{\mathcal X}(x)\cup\eta^{a'',j}_{\mathcal X}(y),$$ where the sum is over the pairs of integers $a',a''\ge0$ with $a'+a''=a$.
5. Unit. If $v\in T^0(X)$ satisfies $v_k=1$ for every $k\ge0$, then $h^{0,0}_{\mathcal X}(v,\varphi)=\varphi(1)$ for every $\varphi\in H^0_0(X/K)^*$, where $1$ on the right is the unit of $H^0_0(X/K)$.
6. First Chern classes. Let $(f,u)$ be a presentation of a line bundle on $\mathcal X$, in the sense of ([Logarithmic first Chern class of a line bundle presented by a cocycle of units](https://andrewodesky.com/rh/lean/CrystallineSemistableComparison.HT.IsDlogFirstChernClass/)), such that $f$ is étale and the open subschemes of $\mathcal X$ over which $f$ has a section cover $\mathcal X$. Then $(f,u)$ has an untwisted étale first Chern class in $T^2(X)$, as the introduction defines it by means of the system $(\zeta_k)$, and the pullback of $(f,u)$ to $X$ has exactly one logarithmic first Chern class $c\in H^2_1(X/K)$. For every untwisted étale first Chern class $v$ of $(f,u)$, $$h^{1,2}_{\mathcal X}(v,\varphi)=\varphi(c)\quad\text{for all }\varphi\in H^2_1(X/K)^*,\qquad h^{a,2}_{\mathcal X}(v,\varphi)=0\quad\text{for all }a\ne1\text{ and }\varphi\in H^2_a(X/K)^*.$$
7. Injectivity. For every integer $n\ge0$ such that $V^n(X)$ is finite-dimensional over $\mathbb Q_\ell$, the map $\kappa^n_{\mathcal X}$ is injective.
8. Top degree. Let $d\ge0$, and suppose that $X$ is connected and smooth of relative dimension $d$ over $K$. If $V^{2d}(X)$ is finite-dimensional over $\mathbb Q_\ell$, then the $\mathbb C_\ell$-linear map $$V^{2d}(X)\otimes_{\mathbb Q_\ell}\mathbb C_\ell\longrightarrow H^{2d}_d(X/K)\otimes_K\mathbb C_\ell,\qquad v\otimes\lambda\longmapsto\lambda\,\eta^{d,2d}_{\mathcal X}(v),$$ is injective.
9. Surjectivity and dimensions. Suppose that $\mathcal X$ is smooth of relative dimension $d$ over $\mathcal O_K$ for some integer $d\ge0$. Then for every integer $n\ge0$ the map $\kappa^n_{\mathcal X}$ is surjective, and $$\dim_{\mathbb Q_\ell}V^n(X)=\sum_{a=0}^{n}\dim_KH^n_a(X/K),$$ where the left-hand side is read as $0$ if $V^n(X)$ is not finite-dimensional over $\mathbb Q_\ell$.
