---
{
  "module": "src/Formalism/LocalRingCardinality/DataNChoice.lean",
  "declarations": [
    "Formalism.BasicNotions.NChoice"
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

## Twist period lattices and coefficient comparisons

[Definition / hypothesis ARAK.D124](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)

Hypothesis (twist period comparisons). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)), ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)), and ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) for the same datum. Write $K\hookrightarrow\mathbb C$ for the coefficient field, $K_0\subseteq K$ for its specified base field, and $G_E$ for the absolute Galois group of the CM field $E$. A finite place $w$ of $K$ has conjugate $\bar w$, residue prime $p_w$, tuple $\mu_w$ and twisting tuple $\nu_w$.

For a twist index $i$, write $O_i^0$ for its finite base coefficient DVR, $O_i$ for its complete coefficient DVR and $O_{i,k}$ for its chosen cyclotomic extension, as in ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)). Write $$\operatorname{Art}_{i,Q}:G_E\longrightarrow R_{i,Q}$$ for the specified surjection to the finite anticyclotomic $\ell_i$-primary quotient associated with a finite set $Q$ of places of $E$. Its kernel is open and it is unramified outside $Q$; its defining universal property is stated in ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)).

At every $w$, choose a twist index $i_w$ with $\ell_{i_w}=p_w$, a side $\beta_w\in\{+,-\}$, a finite set $Q_w$ of places of $E$, a nonnegative integer $k_w$, and a character $$\psi'_w:R_{i_w,Q_w}\longrightarrow O_{i_w,k_w}^{\times}.$$ Put $O'_w=O_{i_w,k_w}$ and $\psi_w=\psi'_w\circ\operatorname{Art}_{i_w,Q_w}$. Choose a DVR $R_w$ with compatible algebra structures over $O_{i_w}$ and $O'_w$, such that $O'_w\to R_w$ is injective, finite and local. Put $F_w=\operatorname{Frac}(R_w)$. Choose an embedding $\jmath_w:K\hookrightarrow F_w$ satisfying $$v_w(a)\ge0\quad\Longleftrightarrow\quad\jmath_w(a)\in R_w\qquad(a\in K).$$

The rational coefficient spaces $T^K_{\mu,j}$, their complex realizations $j_{\mu,j}:T^K_{\mu,j}\to T_{\mu,j}$, and their finite sets of integral generators $\mathcal G_{\mu,j}\subset T_{\mu,j}$ are the choices in ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). The period spaces $V^{\rm per}_{i,j,b,k,Q,\psi}$ and their integral modules $M^{\rm per}_{i,j,b,k,Q,\psi}$ are the choices in ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)). For every $w$ and every integer $j\ge0$, choose a $\jmath_w$-semilinear map $$f_{w,j}:T^K_{\nu_w,j}\longrightarrow F_w\otimes_{O'_w}V^{\rm per}_{i_w,j,\beta_w,k_w,Q_w,\psi_w}.$$ Whenever $\mu_w\ne\mu_0$ and $1\le j\le m$, require that $f_{w,j}$ carry every $K$-basis to an $F_w$-basis and that $$\operatorname{span}_{R_w} \{f_{w,j}(x):x\in T^K_{\nu_w,j},\ j_{\nu_w,j}(x)\in\mathcal G_{\nu_w,j}\} =\operatorname{span}_{R_w} \{1\otimes z:z\in M^{\rm per}_{i_w,j,\beta_w,k_w,Q_w,\psi_w}\}.$$ The coefficient choices must agree with the local Galois data. For every local Galois index $a$ at the coefficient place $w_a$, require its twist index, side and auxiliary set to equal $i_{w_a},\beta_{w_a},Q_{w_a}$. There is one family of characters $\Xi_w:G_E\to K^\times$, indexed by all coefficient places, such that $$\Xi_{\bar w}=\Xi_w,\qquad \jmath_w(\Xi_w(g))=\psi_w(g)\quad(w,\ g\in G_E),$$ where the right side is mapped from $O'_w$ into $F_w$. For every local Galois index $a$, its coefficient embedding $\kappa_a:K\hookrightarrow\operatorname{Frac}(O_a^{\rm Gal})$ also satisfies $$\kappa_a(\Xi_{w_a}(g))=\psi_a^{\rm Gal}(g)\qquad(g\in G_E),$$ where $O_a^{\rm Gal}$ and $\psi_a^{\rm Gal}$ are its coefficient ring and selected twisting character in ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)).

The embeddings must agree on $K_0$. Let $\iota_{i,+},\iota_{i,-}:K_0\hookrightarrow\operatorname{Frac}(O_i^0)$ be the two chosen embeddings. Let $\lambda_w:\operatorname{Frac}(O_{i_w}^0)\hookrightarrow F_w$ be induced by $$O_{i_w}^0\longrightarrow O_{i_w}\longrightarrow O'_w\longrightarrow R_w.$$ Require $$\jmath_w|_{K_0}=\lambda_w\circ\iota_{i_w,\beta_w}.$$

Finally, for every twist index $i$, integer $j\ge0$ and side $b\in\{+,-\}$, choose a subset $\mathcal D^0_{i,j,b}$ of its theta-input set. The finite group $G_{\rm fin}$, its subgroup $U$, its actions, the characters $\psi_{i,b}$ and the theta vectors $\theta_d$ are those of ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)). Require $$u\cdot\theta_d=\psi_{i,b}(u)\theta_d \qquad(d\in\mathcal D^0_{i,j,b},\ u\in U).$$
