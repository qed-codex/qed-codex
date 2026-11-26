---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/LevelGatherings/CompletionIntegersIff.lean",
  "declarations": [
    "Formalism.L2.G.LocId"
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

## Local group completions and stabilizers

[Definition / hypothesis PHT.D194](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.GLevTie/)

Hypothesis (local group completions and stabilizers). Use ([Integral level lattices and their class representatives](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ColLevel/)) and ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)). Write $G=\mathrm U(h)$ for the rank-$k$ unitary group, $L_b$ for its specified integral lattice, and $U_v$ for its local levels. Fix a natural number $p$ and a local polynomial setting with rank $d$, places $a$, rings $W_v\subset Q_v$, component set $C$, groups $\Gamma_c$, and representations $A_{c,v}$. Require $d=k$.

Choose a bijection $v\mapsto\mathfrak p_v$ from $\{0,\ldots,a-1\}$ to the finite places of $F$ containing $p$, and ring isomorphisms $$e_v:Q_v\xrightarrow\sim F_{\mathfrak p_v}$$ such that $x$ belongs to the image of $W_v$ if and only if $e_v(x)\in\mathcal O_{F_{\mathfrak p_v}}$. For every $\mathfrak p\mid p$, choose a ring isomorphism $$s_{\mathfrak p}:E\otimes_F F_{\mathfrak p}\xrightarrow\sim F_{\mathfrak p}\times F_{\mathfrak p}$$ carrying conjugation to exchange of factors and $1\otimes b$ to $(b,b)$ for every $b\in F_{\mathfrak p}$. Choose $f_{\mathfrak p}\in\mathrm{GL}_k(F_{\mathfrak p})$. The first projection under $s_{\mathfrak p}$ of the completed lattice $L_b$ is exactly $f_{\mathfrak p}\mathcal O_{F_{\mathfrak p}}^k$.

Put $$U^{(p)}=\{g\in G(\mathbb A_{F,f}):g_{\mathfrak q}\in U_{\mathfrak q}\text{ for every }\mathfrak q\nmid p\}.$$ Choose $y_c\in G(\mathbb A_{F,f})$ for $c\in C$, with $(y_c)_{\mathfrak p}=1$ at every $\mathfrak p\mid p$, such that $$C\longrightarrow G(F)\backslash G(\mathbb A_{F,f})/U^{(p)},\qquad c\longmapsto[y_c]$$ is a bijection. There are injective homomorphisms $\gamma_c:\Gamma_c\to G(F)$ with image $$G(F)\cap y_cU^{(p)}y_c^{-1}.$$ Require, for every $c,v,\gamma\in\Gamma_c$, $$e_v(A_{c,v}(\gamma))=f_{\mathfrak p_v}^{-1}\operatorname{pr}_1s_{\mathfrak p_v}(\gamma_c(\gamma))f_{\mathfrak p_v}.$$ Field maps in this equation act entrywise; the equality of ranks identifies the coordinate indices.

The following version with a common completion is also used. Choose one ring $W$, one field $Q$ with a $W$-algebra structure, a bijection $v\mapsto\mathfrak p_v$, isomorphisms $e_v:Q\simeq F_{\mathfrak p_v}$, splittings $s_{\mathfrak p}$ and frames $f_{\mathfrak p}$ satisfying precisely the completion, conjugation, scalar and lattice conditions above. This version does not choose component representatives or stabilizer maps. Its additional level condition, when imposed, is that every unitary $x\in G(F_{\mathfrak p})$ satisfies $$x\in U_{\mathfrak p}\ \Longleftrightarrow\ f_{\mathfrak p}^{-1}\operatorname{pr}_1s_{\mathfrak p}(x)f_{\mathfrak p}\in\mathrm{GL}_k(\mathcal O_{F_{\mathfrak p}}).$$ Membership on the right means that both the matrix and its inverse have integral entries.
