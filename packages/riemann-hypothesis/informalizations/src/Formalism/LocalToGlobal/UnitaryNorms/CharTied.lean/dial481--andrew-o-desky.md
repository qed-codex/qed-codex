---
{
  "module": "src/Formalism/LocalToGlobal/UnitaryNorms/CharTied.lean",
  "declarations": [
    "Formalism.L2.Host.CharFrame",
    "Formalism.L2.Host.TupTied"
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

## Hecke characters in recursive realizations

[Definition / hypothesis ARAK.D201](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)) and ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Write $E/F$ for the CM extension, $E_0=\mathbb Q(s_d)$ for the quadratic subfield, $g_0,g_1$ for the generator rational primes, $p_\delta,p' _\delta$ for the two designated auxiliary rational primes, $\Psi$ for the fixed CM type, and $e_j(\tau)$ for the stage weights, with $0\le j<m$.

A Hecke character here is a continuous homomorphism $\mathbb A_E^\times\to\mathbb C^\times$ trivial on diagonal $E^\times$. Write $\chi_P$ for its local component at a finite place and $\chi_\infty(k)$ for the product of its infinite components on $k\in E^\times$. Tame means trivial on $1+\mathfrak p_P$; unramified means trivial on $\mathcal O_{E,P}^\times$. Its restriction is trivial on $F$ when, for every finite or infinite $F$-place and every $a\in F^\times$, the product of its local components over that place on $a$ is $1$.

An auxiliary twisting character with residue prime $\ell$ and finite auxiliary set $Q$ is a Hecke character whose order divides $\ell^a$ for some $a\in\mathbb N$, whose restriction on $F$ is trivial, which is tame at every finite place, ramified at exactly $Q$, identically trivial as a local character above $\ell$, and for which every $P\in Q$ satisfies $P\ne\bar P$.

Hypothesis (character frame). Choose primes $\bar P_a$ of $E_0$ above $g_a$, injective characters $\omega_a:(\mathbb Z/g_a\mathbb Z)^\times\to\mathbb C^\times$, and Hecke characters $\mu_{0,j},\eta,\chi_\Psi,\delta,\delta'$ of $E$. Require that every $\mu_{0,j}$ be unitary, have trivial restriction on $F$, be tame at every finite place and be unramified away from $g_0g_1$. The numbers $-2e_j(\tau)$ are integers and $$\mu_{0,j,\infty}(k)=\prod_{\tau\in\Psi}\left(\frac{\tau(k)}{|\tau(k)|}\right)^{-2e_j(\tau)}.$$ For $P$ above $\bar P_a$ and each natural number $b$ prime to $g_a$, require $$\mu_{0,j,P}(b)=\omega_a(b\bmod g_a)^{-2(j+1)}.$$ Require $\eta$ to be unitary and unramified at every finite place, with $$\eta_\infty(k)=\prod_{\tau\in\Psi}\frac{\tau(k)}{|\tau(k)|}.$$ For $a\in F^\times$ and a finite $F$-place $v$, the product of its local components above $v$ is $(-1)^{\operatorname{ord}_v(a)}$ if exactly one $E$-place lies above $v$, and $1$ otherwise. At an infinite $F$-place it is the sign of the corresponding real embedding of $a$. Require $\chi_\Psi$ to be unitary, unramified at every finite place, have trivial restriction on $F$, and satisfy $$\chi_{\Psi,\infty}(k)=\prod_{\tau\in\Psi}\left(\frac{\tau(k)}{|\tau(k)|}\right)^2.$$

Each of $\delta,\delta'$ has finite order, trivial restriction on $F$, and is tame everywhere. The first is unramified away from $p_\delta$ and the second away from $p'_\delta$. At every place above its designated prime, its local character on units has exponent exactly $15$: for every natural number $n$, all these unit values have $n$th power $1$ if and only if $15\mid n$.

Hypothesis (characters of twist labels). Let $\mathcal T$ be the member's twist-label set, with base label $\mu_0$, special labels $\mu_*,\mu_*'$ and selected labels $\mu_w,\mu_w^{\rm tw}$ at coefficient places. Choose an injective map $\xi:\mathcal T\to\{\text{Hecke characters of }E\}$. Every $\xi_\mu$ has finite order, trivial restriction on $F$ and is tame everywhere. Choose Hecke characters $\psi_w$ and require $$\xi_{\mu_0}=1,\quad\xi_{\mu_*}=\delta,\quad\xi_{\mu_*'}=\delta',\quad\xi_{\mu_w^{\rm tw}}=\delta_{\ell_w}\psi_w,$$ where $\delta_\ell=\delta'$ if $\ell=p_\delta$ and $\delta_\ell=\delta$ otherwise. If $\mu_w=\mu_0$, require $\psi_w=1$. Otherwise require $\psi_w$ to be an auxiliary twisting character with residue prime $\ell_w$ and the selected auxiliary set $Q_w$ of ([Twist period lattices and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)). The stage-$j$ character of a twist is $\mu_{0,j}\xi_\mu$.
