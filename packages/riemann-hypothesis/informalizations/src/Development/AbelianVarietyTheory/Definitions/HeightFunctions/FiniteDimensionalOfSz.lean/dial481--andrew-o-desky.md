---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/HeightFunctions/FiniteDimensionalOfSz.lean",
  "declarations": [
    "GlobalTheory.FieldSize.IsRay"
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

## Ray-class extensions and their character values

[Definition / hypothesis ANT.D075](https://andrewodesky.com/rh/lean/GlobalTheory.Published.RayClassFieldSt/)

Let $K$ be a number field, let $L/K$ be a finite abelian Galois extension of number fields, and put $G=\operatorname{Gal}(L/K)$. Write $\mathcal O_K,\mathcal O_L$ for their rings of integers and $N\mathfrak p=\#(\mathcal O_K/\mathfrak p)$ for the absolute norm of a nonzero prime ideal $\mathfrak p\subset\mathcal O_K$.

**Inertia, Frobenius and character values.** An element $\tau\in G$ belongs to inertia above $\mathfrak p$ if there is a prime ideal $\mathfrak P\subset\mathcal O_L$ above $\mathfrak p$ such that $$\tau(x)-x\in\mathfrak P\qquad(x\in\mathcal O_L).$$ The extension is *unramified at $\mathfrak p$* if every such $\tau$ is the identity. An element $\sigma\in G$ is an *arithmetic Frobenius above $\mathfrak p$* if there is a prime ideal $\mathfrak P\subset\mathcal O_L$ above $\mathfrak p$ such that $$\sigma(x)-x^{N\mathfrak p}\in\mathfrak P\qquad(x\in\mathcal O_L).$$

For a character $\chi:G\to\mathbb C^\times$, define its value $a_\chi(\mathfrak p)\in\mathbb C$ as follows. If $\chi$ is trivial on every element belonging to inertia above $\mathfrak p$ and an arithmetic Frobenius $\sigma$ exists there, put $a_\chi(\mathfrak p)=\chi(\sigma)$, viewed as a complex number. The value is independent of the chosen Frobenius. In all other cases put $a_\chi(\mathfrak p)=0$.

For a nonzero integral ideal $I=\prod_{\mathfrak p}\mathfrak p^{v_{\mathfrak p}(I)}$, define $$a_\chi(I)=\prod_{\mathfrak p:\,v_{\mathfrak p}(I)>0}a_\chi(\mathfrak p)^{v_{\mathfrak p}(I)}.$$ The product is finite; $a_\chi(\mathcal O_K)=1$.

**Ray-class conditions.** Fix a nonzero integral ideal $\mathfrak m\subseteq\mathcal O_K$. Say that $L/K$ satisfies the *ray-class conditions modulo $\mathfrak m$* if all three statements hold:

1. The extension is unramified at every nonzero prime $\mathfrak p\nmid\mathfrak m$.
2. The elements that are arithmetic Frobenius above some nonzero prime $\mathfrak p\nmid\mathfrak m$ generate $G$.
3. For every nonzero integral ideal $I$ with $I+\mathfrak m=\mathcal O_K$, the equality $a_\chi(I)=1$ for every character $\chi:G\to\mathbb C^\times$ is equivalent to the existence of $\alpha,\beta\in\mathcal O_K$ such that $$\alpha\ne0,\quad\beta\ne0,\quad(\alpha)+\mathfrak m=(\beta)+\mathfrak m=\mathcal O_K,\quad\alpha-\beta\in\mathfrak m,$$ $$I(\beta)=(\alpha),\qquad \varphi(\alpha)\varphi(\beta)>0\quad\text{for every real embedding }\varphi:K\hookrightarrow\mathbb R.$$ Here $(\alpha)$ and $(\beta)$ are principal integral ideals. If $K$ has no real embeddings, the sign condition is vacuous.

**The existence hypothesis.** The *ray-class-field existence hypothesis* asserts that, for every number field $K$ and every nonzero integral ideal $\mathfrak m\subseteq\mathcal O_K$, there is a finite abelian Galois extension of number fields $L/K$ satisfying these ray-class conditions modulo $\mathfrak m$.
