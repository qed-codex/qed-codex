---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemClosureOfJumps.lean",
  "declarations": [
    "GlobalTheory.HodgeTateCochar.mem_closure_of_jumps",
    "GlobalTheory.HodgeTateCochar.poly_vanish"
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

## A cocharacter with the Hodge jumps in each local Zariski closure

[Theorem PHT.0330](https://andrewodesky.com/rh/lean/GlobalTheory.HodgeTateCochar.mem_closure_of_jumps/)

Let $\ell$ be prime and fix the source's local prime and integral period data with their compatibility condition. Let $E$ be a number field, $\Omega/E$ a field extension, and $G_w\le\operatorname{Aut}_E(\Omega)$. Choose a topological commutative $\mathbb Z_\ell$-algebra $O$ and the source's local completion bridge identifying $G_w$ with $G_K$ for a finite extension $K/\mathbb Q_\ell$. Let $$r:G_w\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell),\qquad \tau:E\hookrightarrow\overline{\mathbb Q}_\ell.$$ Assume $r$ has a finite-coefficient-field model, containing the bridge's coefficient field, which is de Rham, and that a local embedding inducing $\tau$ gives its de Rham filtration jumps the multiset $J\subset\mathbb Z$, with $|J|=a$.

There are $P\in\operatorname{GL}_a(\mathbb C_\ell)$ and $k_1,\ldots,k_a\in\mathbb Z$ with multiset $J$ such that the following holds. For every finite extension $K'\supseteq K$ in the fixed local algebraic closure and every polynomial $f$ in the $a^2$ matrix entries over $\mathbb C_\ell$, if $f(r(g))=0$ whenever the image of $g$ in $G_K$ lies in $G_{K'}$, then $$f\!\left(P\operatorname{diag}(t^{k_1},\ldots,t^{k_a})P^{-1}\right)=0\qquad(t\in\mathbb C_\ell^\times).$$ The entries of $r$ are included from $\overline{\mathbb Q}_\ell$ in $\mathbb C_\ell$.

## Polynomial relations on a Galois image vanish on its weight cocharacter

[Theorem PHT.0440](https://andrewodesky.com/rh/lean/GlobalTheory.HodgeTateCochar.poly_vanish/)

Let $\ell$ be prime, fix the compatible local period and $A_{\mathrm{inf}}$ data of ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)), and denote their cyclotomic character by $\chi_{\mathrm{cyc}}:G_{\mathbb Q_\ell}\to\mathbb Q_\ell^\times$. Let $K,L,K'\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$, with $K,L\subseteq K'$, and let $$r:G_K\to\operatorname{GL}_m(L),\quad P\in\operatorname{GL}_m(\mathbb C_\ell),\quad k_1,\ldots,k_m\in\mathbb Z.$$ Suppose for every $g\in G_{K'}$, $$r(g)\,g(P)=P\operatorname{diag}(\chi_{\mathrm{cyc}}(g)^{-k_1},\ldots,\chi_{\mathrm{cyc}}(g)^{-k_m}),$$ where $G_K$ acts on $\mathbb C_\ell$ and on matrix entries. If a polynomial $f\in\mathbb C_\ell[X_{ab}:1\le a,b\le m]$ vanishes on $r(G_{K'})$, then $$f\!\left(P\operatorname{diag}(t^{k_1},\ldots,t^{k_m})P^{-1}\right)=0\qquad(t\in\mathbb C_\ell^\times).$$
