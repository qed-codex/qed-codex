---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/DataG.lean",
  "declarations": [
    "Formalism.MainNotions.G.GAtP",
    "Formalism.MainNotions.G.Level",
    "Formalism.MainNotions.G.Places"
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

## Local polynomial lattice settings

[Definition / hypothesis PHT.D136](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)

Hypothesis (local polynomial lattice settings). Fix a natural number $p$. Choose a DVR $O$ and an $O$-algebra $K$ that is a field, a natural number $a$, a finite component set $C$, a nonnegative integer $e$, integers $m_0,r_0\ge0$, and an element $w\in O$. For every $0\le v<a$, choose an integer $n_v\ge0$, a DVR $W_v$ with fraction field $F_v$, field embeddings $\iota_v$, ring homomorphisms $j_v$ and field automorphisms $\sigma_v$, $$\iota_v:F_v\hookrightarrow K,\qquad j_v:W_v\to O,\qquad \sigma_v:F_v\xrightarrow\sim F_v,$$ and integer rows $\lambda_{v,s,0}\ge\cdots\ge\lambda_{v,s,m_0}$ for $0\le s<n_v$.

For each $0\le v<a$, impose all of the following conditions. The number $p$ is prime with $p\ge5$, the integer $n_v$ is even and at least two, $K$ is a fraction field of $O$, and $p$ is a uniformizer of $W_v$. The ring $W_v$ is $p$-adically complete, and $$|W_v/pW_v|=p^{n_v},\qquad \sigma_v^{n_v}=1,\qquad \sigma_v(x)\equiv x^p\pmod{pW_v}\quad(x\in W_v).$$ For this same $v$, require that $O$ be complete for its maximal ideal, that $j_v$ be finite, and that $$\iota_v(x)=j_v(x)\text{ in }K\quad(x\in W_v),\qquad w^2=p.$$ The equality uses the specified fraction-field maps.

For each component $c\in C$, choose a group $\Gamma_c$, representations $$a_{c,v}:\Gamma_c\longrightarrow\mathrm{GL}_{m_0+1}(F_v),$$ and a character $\chi_c:\Gamma_c\to O^\times$.
