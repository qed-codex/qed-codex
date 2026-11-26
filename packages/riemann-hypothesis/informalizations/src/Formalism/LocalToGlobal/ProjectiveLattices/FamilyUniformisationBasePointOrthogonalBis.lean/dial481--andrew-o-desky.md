---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/FamilyUniformisationBasePointOrthogonalBis.lean",
  "declarations": [
    "Formalism.L2.Pj.LawsJ"
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

## Scalar normalizations and adelic period identifications

[Definition / hypothesis ARAK.D199](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsJ/)

Hypothesis (scalar normalizations and period identifications). Impose Hypothesis (original moduli and cusp norms) in ([Original moduli uniformizations and cusp norms](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM/)). At every natural stage $j$ and embedding $\sigma:K_0\hookrightarrow\mathbb C$, the original datum also chooses complex scalars $c_{j,\sigma,c}$ on its domain labels, a unitary character $$\chi_{j,\sigma}:(\mathbb A_F\otimes_FE)^\times\longrightarrow\mathbb C^\times,$$ complex matrices $x_{0,j,\sigma}(\tau)\in M_r(\mathbb C)$ for every embedding $\tau$ of $E$, and an $\mathcal O_E$-linear map $\iota_j:\Lambda_j\to E^r$. The map $\iota_j$ is chosen once at each stage and is independent of $\sigma$. The conditions below apply for $1\le j\le m$ and every good embedding $\sigma$, except that the integral-extension condition applies at every selected stage without an archimedean embedding.

Require $|c_{j,\sigma,c}|=1$. For every $g\in G_j=U(W_j)(\mathbb A_F)$ there exists $x\in(\mathbb A_F\otimes_FE)^\times$ with $$x=\det(g)\bar x.$$ For every such solution, require $\mu_{j,\sigma}(g)=\chi_{j,\sigma}(x)$. Let $\sigma_0:K_0\subset\mathbb C$ be the distinguished embedding. For every $x$ with infinite component one and finite component in $(\widehat{\mathcal O_E})^\times$, there is $y\in K_0$ with $$\chi_{j,\sigma_0}(x)=\sigma_0(y),\qquad\chi_{j,\sigma}(x)=\sigma(y).$$

The following integral-extension condition uses the integral framed points defined in ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)). For every prime $\lambda$ of $K_0$, complete characteristic-zero DVR $R$ of finite residue field, embedding $K_0\hookrightarrow L=\operatorname{Frac}R$, and $e>0$ satisfying $v_R(a)=e\,v_\lambda(a)$ on $K_0$, every framed moduli point over $L$ acquires an integral realization after an extension of fields and a triangular change of frame. More precisely, there are another such DVR $R'$ with finite residue field, an embedding $K_0\hookrightarrow L'=\operatorname{Frac}R'$, a positive integer $e'$ with $v_{R'}(a)=e'v_\lambda(a)$ on $K_0$, an integral framed point $y'$ over $L'$, a $K_0$-field embedding $\varphi:L\hookrightarrow L'$ carrying $R$ into $R'$, and a triangular change of tangent bases and generating-section scale carrying the scalar extension of the given point to $y'$. No finite-degree condition on $L'/L$ is imposed.

At every domain require $$G_c=-G_{W_j}^T,\qquad\xi_c=-\xi_0,$$ and require $x_{0,j,\sigma}(\tau)$ to have Hermitian Gram matrix $\operatorname{diag}(1^{q_j},-1^{p_j})$ at every domain CM embedding. In addition to its description in ([Original moduli uniformizations and cusp norms](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM/)), the same finite subgroup satisfies $$K_{j,\sigma}=\{k\in G_j:k_\infty=1,\ \forall b\in\bar{\mathfrak b},\ \forall z\in\widehat L_{0,j}:\ (k_f-1)(bz)\in M\widehat L_{0,j}\}.$$ Here $M=g_0g_1$ and $\mathfrak b$ is the original level ideal.

Use the lattice constructions $L(h)$ and $\widehat L(h)$ in ([Adelic frames for unitary moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.Core/)) for $V=W_j$. The chosen map $\iota_j$ is injective, has image $L(1)$, and for some sign $\epsilon\in\{1,-1\}$ satisfies $$E_j(a,b)=\epsilon\operatorname{Tr}_{E/\mathbb Q}\{\xi_0h_{W_j}(\iota_ja,\iota_jb)\},$$ where the chosen basis identifies $W_j$ with $E^r$. There is a period family, with all its conditions defined in ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)), together with one assignment $c\mapsto b(c)$ from domains to its integral-module types and isomorphisms $\phi_c:\Lambda'_{b(c)}\simeq\Lambda_c$. These satisfy the trace-pairing identity, the explicit period-coordinate formula and the equality of its coordinate derivatives with the framed-point tangent basis in ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)), at the original level $(M,\mathfrak b,A)$. Choose continuous extensions $\theta_{c,\tau}$ of the CM embeddings to the infinite adelic tensor ring, with the continuity and restriction conditions of ([Adelic frames for unitary moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.Core/)).

For every $h\in G_j$, some $\gamma\in G_j(F)$ has, for the domain $c$ selected by $\delta_{j,\sigma}(h)$, $$\Lambda_c=L(\gamma h),\qquad\widehat{\phi_c(t_{b(c)}a)}-(\gamma h)_f\widehat{\iota_j(a)}\in M\widehat L(\gamma h)\quad(a\in\bar{\mathfrak b}\Lambda_j),$$ $$\delta_{j,\sigma}(h)_\tau=(\gamma h)_{\infty,\theta_{c,\tau}}\,x_{0,j,\sigma}(\tau).$$ Hats on vectors denote their finite-adelic images. The period-family choices and continuous extensions can depend on $j$ and $\sigma$, while these conditions use the already chosen $x_{0,j,\sigma}$ and $\iota_j$.
