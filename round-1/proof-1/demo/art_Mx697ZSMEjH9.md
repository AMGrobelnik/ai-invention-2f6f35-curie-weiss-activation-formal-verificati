# CWA Formal Proof: Banach Convergence, IFT Gradient, Bias Bound

> **[Run in Lean Playground](https://live.lean-lang.org/#codez=JYWwDg9gTgLgBAWQIYwBYBtgCMB0BBAOyXQE8BnYMnAZTAFMBjYYgMQFcCGZgICqBRAB5gAInSjAAbgChQkWIhQZs+IqQpVajZunaduvKgBUJAc14QQdGBIY4AQkgoNZ4aPGRpMuQsXKUcAGFiBjZ0NioxCUkgyzBXeQ8lb1U/DSCQsIicKKkcBDCE90UvFV91AOD0UPDI8TyASQIZOWLPZR81fyoqmuyEOiQCADViNjoihXaUowhIdAhTEnzrW1okBjpYghsN7gJTaWkAWmO4QIB1PDgABSgICAAzAC44Bl5JcVM6TjoAGjgDRYRjgj2gIDCSABQwAJnAsMwyPCIBwYSczkZUFA6HQ4Gg6NA6CAkWCoHAWAAKEAASjgAF48UNUBTBHAANRwABSACoaQDOXBgAQ4BSAAx/ACM1KOp3pdPlCsVSuVKtVavVivRtyQCglr1ykhQUjoSKecAoBFQAPeZCtjMtWo1TudLvVR3QRJASDgqCcBrwMAA+hbUCLWa9ALiEtNeAAk/fVJAG4AAlQboHAhkWp4g4G2hwS08MMrAkaRwH1IT4+iVwZ4M7Pp31kf1BujCOCCMsVquoABMtbgcebCaTFIbODbYDggAwiOAAOTophwBEXtLHaYn7YpxwLcG5IuOUsLtbpXfL65zTZbgcnB4L1NzcQ7IqvI6DK9MHel5d9PYALAOQ4tiKjwcM+dIAHxZhut6smc463tu95wAA9HAvbfuWWEUhe6awXA8EwVuO60vu25Hqh6HHnWZ4vhKGZsFgPoYTgMJSIG7x8PAvZdpxnwKKgAEREKn4Sl2ADtoIcG28AkAA3HAbZ7CmG4hjeACOcCluWklQAA7nAADa455hpAC6CkSAc7qet6r7RAGHEQLaYYDlGgHxg58Amc5oa4RmQr5tRxbad2uKoDWdYqZenlSI5sFdr+4X9rGsWJvA/m3rOC5Lh+a4IcRu5kYe1LBbR/n2XFraFaVj7gM+FKVelgYfl+iWVuFAGpcOXkgWBrKQdBOb4RyBVTkhpWURhtHnpl7asqNRHjSRe4HhRaEYc+NFYXROBIDCcJ9g+bGSE5XHobxHziPAglwMJBxwGJOlSSugiyQpSlcNF6amXQmmhbpBnGapgXmZZIk2SAXoVj1VWBjATKuZG0aDmlSbjgjloijWhE5pj+ZwAAelRW0he1PamSuA4+S5rKAAZEcCiieQ0/b5gaQEiBbLnQADk5PhZmUVNY5madj+HU+nmzPC0GUti2Fkts0KkgebD6V9cKJD0lB/lSyQ1KAN4EACda7HOOouUTTBPE5tRa0ageY4Mriu2i1Eziz2YD3HC3XARSoGa9r30BVjWtkVbWmGybM0s4+tOrbrvlfsb7LBxbxXm4Fz5oRHrI25Nds7agIY4BC6Au6ggbK5dzTXT6XsQHC92iRJL0yVpllAxjTIacGoMnU5toWaCwB0OgMJ9+Arf6UZ3eWr3akD3mZn2xLqDAD7wdy0T6EEWnWd57vDKRfWG6mWQ6nBoxffzxfHa0Y8o/j5P8Q7QQmBEBIaCz2fbMcx2K9pAeiht6NijxHjiB+NwJAWAPTw0RvqYA4DIE7GYLA3EEZg74xPF2AO4EdYy3gVjLmYCIHYlQTAj0AYZRnFdHQ+hTotQ3B1NxV42DKCPWOAAGWAGAMgDB14wAAF6OgYWI8R8pIbQzIIwSuF8Wq8FaiyNyKMmaABMiR6e857W13lFEs/MfQb2pr/eONstEg2ITvfsx9mZW2DJfMg181J33lklSWU4op2P/vLGewM8Y9z+jfSuS9fIAgHpAPSfwY68DoFfLAgYToigiW7QMQjxAQF3g7MA3MebUhXuWJAYAwCkDgAPAgijFxwEDCKeR5SCCtUDJhd+QodTAG/oZWpFTPz+VFnkqR3oZECPsYGOBMSkZwHcq8HGWDEaH37Bok+8JQof1ae0zp9TKn+WwQWQBwDob1PKVAEACSExEMrh6cZky4CADQCGECYZnEOuYAKII4ALOZvo8svjGpoyDNs46CZ8kK1QEzKKgy5GXzqa1Vxa9FlguGaMqmPiga2ggAZa5FJpnaOfPnZ59I4CAAvyTFG5tlWIBMCwAl+SgnuCAJZtEKD1UMgc8EAI5ysvBMuepzLg6HOOU8BRGzPzArMoCz6QYQCNw4k4G6YkgG2XtOc3h/DBFCIuG0yuYzXg8L4QItpKq1WaKxdtOAmBtXKtVWgQMfKmVHJOdEEZuJSEoOgegs5cBrXHLuXa/G9qaFygkf610TCWFwAAMyvEpDSPF+NlEch5JGjhnJuGKp1cIuAsI3i8F2FwCGsoA15udP041QoRnJuVZc2kABvAUkYAC+L5OQgsZq8rk0ZaJaqVbq81oZ8WcjJQ2yl/swI0sGgtLkq1I16NCr4k1HbhFdqruAhJlAgxwLLoCoUNgMneiwF2elU5eAlL8emNiZBWzqRZXOHysSQAAGtAVuNDK8UdAp9zejODGsd+4sC0gZC+kUb74TRhCnAKyhxPlAztDAsggYy7QiwNBq1XSfQNt2XKlgJbTW6vLXAKtbk62NQbQOdRLb62RTHQAHkeq2na7aU16u/j2vtooB14OHVBLFH6/00iA7Sj24VmbepnXR+dMS6rjQ/hh2dQjnyoAbZhPdcAD1a0Mqyq9lqVwAhiTBsIZk003QMagP6xj/FY1nIO4UbHnyxvHT+l6cBLMcefTZ5mUBHjoC7Ppb0hlDPqV0ygH0hb0OcSzfsbp4YJmVurRM/DsnG1M0o5yNcsmyMCko1KWstFAiZqgHsESXaCW9uNbEvl6Abr9o1vZoOjnU5ccmpOmup6oBsC4NAVuoqYMSoYFK5DT04CSVFeSSTdGGqjMeCMsropaTJd9fm2baotSYgJNiGlepzhXDgI4IgAjyTAEEHQGExwbgQA3XARbhIQCiLm1dhURx8TnbeHpJAgYsBDA2H5cL7lcO1vrXFuACWkuchS39qjGWdqAGAiAAhPZ4MCMySRgBNV6z+5jmnp1LZlHsP3mhQfQwZmQXsu5YeqyWLPWuwengCwZmrGqvEsRpxmzXYIi4iyzsHL2aDhdpwI/PbMIjsncpw7LsA38UOy57t/bfOdhVzICwcXvOYAAjwVrVAWtBqi+5xL47UuODAHUuMH0JByUzeuyboNCg/yvDwOgb4WAcvAFx4Z9A9AoAkmgICYEl2TdzcLVpxx8TOTBhe1AdmzkcNRYjDFwjrx4skYI0DtLmFzzQaDyol8ZBfsaOT2jtPZGs9kgWdRrCMfpl/rz1jt1Kyv6oGN1773sozvLfQq8IEIIADiOW2JQPJOCSEnva95tu4Z+7SCgymA76PKX7woDYi+sogUGOdSp4I79/7pGBypZB88Wi5PzTPcX1FIlJn3s1fHTD7PNtt/WDgGP/azMy9oQxXvUve+oCJ93ynsiNYkfX477Zm/PsyZywFMlNd0r8kQD9zEj9XJv8F9X8rEDN08iNm1wCGQ4V1kGkEDc9m1YVZF4VisqZAwDM7lhQpkn9VokQGYQVTwdoKRfdr4A8yAg8Q8kQSdktzQfREDi4pQclcEn4J4FNvNiDAFZQW801rc6BbckB7c7oCBddxgVwyAyBXgyBuQMU2QeQYRbM4Q5BMATRSk8UyAUIMVjgeQyBpQ9lvQR8NI2AjReBAwdc9dYkyAIBwgDBhQKQy84Rw839GpEDo9kCX8ksyBc8X9sCfCSd/DV84919gcpRyofMBwy9P8T99xNC8U0it8do4RUDQiH8S9yDAisciCfgBx8j9wy9KCcEaC6D/dA8dRmDkMmY2Cy9i4mjgiHwVw+ZyxH4x5+C5AjJUAhCycWkq8a9+8B968h9G8w0NtEQNsUQCA0Rc1xj81C1gs2c3DAxsQKAYQbD0BnsFi4QK0ABpPDF8Y4jPOAY4pLY4sjU4hPWiCtR4NyOAQAJMJosXwxsTUBxaMzV9V8VjiyULjKVHg38K1jlCkG5WRYCzjfDMdXhniYSGRYDC9ywAAfCEope4OCaHVHKANE5tNExEwMSE7EveTEqEgkvIvea4oovjH0YgpAtLGk8vSvNVDzIGOBAeJBR4QAAIIGSfhAVZRfisMsBDjXgiSqQSSsSIBdwzhHgpS8TqQCSNFTj9wMTpSoTySz98SDNviJTiTSTZS95iS8SVSrjVoNSjScTYCCT6si415pYvjeFWJl17VtNy4KSyTYC6V+ilMf4cwT0z0L01Nb0/N9Mdo2S0AuxZQFSUS8VYCARnC4BJSvTZTaQzhbTm01SUy0ybSdS0SOSBi8TwyfQTUYyMQJAhhTAPQJS8ztSzTCT6z5SpTrTlTU5UzNTsSMzcTYdCz6TUAbBgABwrSZT8zGyNFRytT5TodrSCSOQiTZyxyGy+y6SsIutqhcyuzjTMyCyY5ywGQ0TWzlyZy8zaQOR/Ylzpzey0c7TgNQMWpHgY5qlJzmzQQrzsT5yUzDSTybz8TmYoMSSDoqkqkKzzhLAEQqYYAMlvgMoJRjhrjuQpyyTdyJzvzjyoSey8z+ygUyASAaUDSPydyiLBACTDy3yfzKSAL4M4knIoYQLCDyxmlP59VDJALIVNk3yUS4NoMOLulKKUKSLqQokdpRKdp2KkNLyuKdS+lpA7tG8GBHsF0gwEQnB7DZDSQaVlFkYw9YSIim0oi2DXgN84idpwTtzoSdS8N4i8TjN0xsF6dkcZKEyZL4jtiRzEdP0hLtS5zsC6BjgAJkizhEtUStzrSVydRzSJR/KupACgU3M8chsy1WQKRRtxtGiptAcDMxTUQRzpKJyY40TPKuMLKsKLKqTsYn8gNaJ1jcs7DtiN49iDjcrUrisviJtMqaxUAEri5YcDN/5XgxRU9mTgrWSRj2TywNzcdkLiLbSY5JzirT82yfKxyKrH9gqeNUAcrFjaIXzsYYqE4S9JpqSNq1yxLISSkB4uT2JEMBUtjgBTBByfRtj9yi0WLoydpqlj4DrJ0R5eiX4xiViJEtRkAhRwKQBIL9tTspiiQ+8gaxFB8lsiQHsnsvQwbtKItdLvtl8mTY8jKKNN9aJZQMVaQABVWQxwkeHnOASAE7NsZdMgcqSHP8tyBHWnLGRyv89HZywAciIib31NpRD/8J94BNLIRBQkRiAbc7cNySlOINAYAoFypAAAIhZvhxjh3zLwgNxnsrpycycqVPgLEp33/zv1yMqtGvKMCJjiSMqu/3/z/1/zgD5p2mJpDVpDwBhEKW4CrGgo9By1+EehitUPgsSy0j4KRB100vhDmO2rhGioCpVpIrVomREtEsWoNth25tsteMKozu8t3N8oWQOqCpI1zrEpmvHNXOLoCuqvLHxUUqexey2wJlYMBzTrsyRKgisOFqgScmn0YHgFZHnysrbolA7tYwspZt6sXyxD0MGkbuUue0RHUqQXBBk0IzYJnrJDnrICNyAA)**

[![Open in Lean](https://img.shields.io/badge/Lean_4-Verify_Proof-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyTDIgMTloMjBMMTIgMnoiLz48L3N2Zz4=)](https://live.lean-lang.org/#codez=JYWwDg9gTgLgBAWQIYwBYBtgCMB0BBAOyXQE8BnYMnAZTAFMBjYYgMQFcCGZgICqBRAB5gAInSjAAbgChQkWIhQZs+IqQpVajZunaduvKgBUJAc14QQdGBIY4AQkgoNZ4aPGRpMuQsXKUcAGFiBjZ0NioxCUkgyzBXeQ8lb1U/DSCQsIicKKkcBDCE90UvFV91AOD0UPDI8TyASQIZOWLPZR81fyoqmuyEOiQCADViNjoihXaUowhIdAhTEnzrW1okBjpYghsN7gJTaWkAWmO4QIB1PDgABSgICAAzAC44Bl5JcVM6TjoAGjgDRYRjgj2gIDCSABQwAJnAsMwyPCIBwYSczkZUFA6HQ4Gg6NA6CAkWCoHAWAAKEAASjgAF48UNUBTBHAANRwABSACoaQDOXBgAQ4BSAAx/ACM1KOp3pdPlCsVSuVKtVavVivRtyQCglr1ykhQUjoSKecAoBFQAPeZCtjMtWo1TudLvVR3QRJASDgqCcBrwMAA+hbUCLWa9ALiEtNeAAk/fVJAG4AAlQboHAhkWp4g4G2hwS08MMrAkaRwH1IT4+iVwZ4M7Pp31kf1BujCOCCMsVquoABMtbgcebCaTFIbODbYDggAwiOAAOTophwBEXtLHaYn7YpxwLcG5IuOUsLtbpXfL65zTZbgcnB4L1NzcQ7IqvI6DK9MHel5d9PYALAOQ4tiKjwcM+dIAHxZhut6smc463tu95wAA9HAvbfuWWEUhe6awXA8EwVuO60vu25Hqh6HHnWZ4vhKGZsFgPoYTgMJSIG7x8PAvZdpxnwKKgAEREKn4Sl2ADtoIcG28AkAA3HAbZ7CmG4hjeACOcCluWklQAA7nAADa455hpAC6CkSAc7qet6r7RAGHEQLaYYDlGgHxg58Amc5oa4RmQr5tRxbad2uKoDWdYqZenlSI5sFdr+4X9rGsWJvA/m3rOC5Lh+a4IcRu5kYe1LBbR/n2XFraFaVj7gM+FKVelgYfl+iWVuFAGpcOXkgWBrKQdBOb4RyBVTkhpWURhtHnpl7asqNRHjSRe4HhRaEYc+NFYXROBIDCcJ9g+bGSE5XHobxHziPAglwMJBxwGJOlSSugiyQpSlcNF6amXQmmhbpBnGapgXmZZIk2SAXoVj1VWBjATKuZG0aDmlSbjgjloijWhE5pj+ZwAAelRW0he1PamSuA4+S5rKAAZEcCiieQ0/b5gaQEiBbLnQADk5PhZmUVNY5madj+HU+nmzPC0GUti2Fkts0KkgebD6V9cKJD0lB/lSyQ1KAN4EACda7HOOouUTTBPE5tRa0ageY4Mriu2i1Eziz2YD3HC3XARSoGa9r30BVjWtkVbWmGybM0s4+tOrbrvlfsb7LBxbxXm4Fz5oRHrI25Nds7agIY4BC6Au6ggbK5dzTXT6XsQHC92iRJL0yVpllAxjTIacGoMnU5toWaCwB0OgMJ9+Arf6UZ3eWr3akD3mZn2xLqDAD7wdy0T6EEWnWd57vDKRfWG6mWQ6nBoxffzxfHa0Y8o/j5P8Q7QQmBEBIaCz2fbMcx2K9pAeiht6NijxHjiB+NwJAWAPTw0RvqYA4DIE7GYLA3EEZg74xPF2AO4EdYy3gVjLmYCIHYlQTAj0AYZRnFdHQ+hTotQ3B1NxV42DKCPWOAAGWAGAMgDB14wAAF6OgYWI8R8pIbQzIIwSuF8Wq8FaiyNyKMmaABMiR6e857W13lFEs/MfQb2pr/eONstEg2ITvfsx9mZW2DJfMg181J33lklSWU4op2P/vLGewM8Y9z+jfSuS9fIAgHpAPSfwY68DoFfLAgYToigiW7QMQjxAQF3g7MA3MebUhXuWJAYAwCkDgAPAgijFxwEDCKeR5SCCtUDJhd+QodTAG/oZWpFTPz+VFnkqR3oZECPsYGOBMSkZwHcq8HGWDEaH37Bok+8JQof1ae0zp9TKn+WwQWQBwDob1PKVAEACSExEMrh6cZky4CADQCGECYZnEOuYAKII4ALOZvo8svjGpoyDNs46CZ8kK1QEzKKgy5GXzqa1Vxa9FlguGaMqmPiga2ggAZa5FJpnaOfPnZ59I4CAAvyTFG5tlWIBMCwAl+SgnuCAJZtEKD1UMgc8EAI5ysvBMuepzLg6HOOU8BRGzPzArMoCz6QYQCNw4k4G6YkgG2XtOc3h/DBFCIuG0yuYzXg8L4QItpKq1WaKxdtOAmBtXKtVWgQMfKmVHJOdEEZuJSEoOgegs5cBrXHLuXa/G9qaFygkf610TCWFwAAMyvEpDSPF+NlEch5JGjhnJuGKp1cIuAsI3i8F2FwCGsoA15udP041QoRnJuVZc2kABvAUkYAC+L5OQgsZq8rk0ZaJaqVbq81oZ8WcjJQ2yl/swI0sGgtLkq1I16NCr4k1HbhFdqruAhJlAgxwLLoCoUNgMneiwF2elU5eAlL8emNiZBWzqRZXOHysSQAAGtAVuNDK8UdAp9zejODGsd+4sC0gZC+kUb74TRhCnAKyhxPlAztDAsggYy7QiwNBq1XSfQNt2XKlgJbTW6vLXAKtbk62NQbQOdRLb62RTHQAHkeq2na7aU16u/j2vtooB14OHVBLFH6/00iA7Sj24VmbepnXR+dMS6rjQ/hh2dQjnyoAbZhPdcAD1a0Mqyq9lqVwAhiTBsIZk003QMagP6xj/FY1nIO4UbHnyxvHT+l6cBLMcefTZ5mUBHjoC7Ppb0hlDPqV0ygH0hb0OcSzfsbp4YJmVurRM/DsnG1M0o5yNcsmyMCko1KWstFAiZqgHsESXaCW9uNbEvl6Abr9o1vZoOjnU5ccmpOmup6oBsC4NAVuoqYMSoYFK5DT04CSVFeSSTdGGqjMeCMsropaTJd9fm2baotSYgJNiGlepzhXDgI4IgAjyTAEEHQGExwbgQA3XARbhIQCiLm1dhURx8TnbeHpJAgYsBDA2H5cL7lcO1vrXFuACWkuchS39qjGWdqAGAiAAhPZ4MCMySRgBNV6z+5jmnp1LZlHsP3mhQfQwZmQXsu5YeqyWLPWuwengCwZmrGqvEsRpxmzXYIi4iyzsHL2aDhdpwI/PbMIjsncpw7LsA38UOy57t/bfOdhVzICwcXvOYAAjwVrVAWtBqi+5xL47UuODAHUuMH0JByUzeuyboNCg/yvDwOgb4WAcvAFx4Z9A9AoAkmgICYEl2TdzcLVpxx8TOTBhe1AdmzkcNRYjDFwjrx4skYI0DtLmFzzQaDyol8ZBfsaOT2jtPZGs9kgWdRrCMfpl/rz1jt1Kyv6oGN1773sozvLfQq8IEIIADiOW2JQPJOCSEnva95tu4Z+7SCgymA76PKX7woDYi+sogUGOdSp4I79/7pGBypZB88Wi5PzTPcX1FIlJn3s1fHTD7PNtt/WDgGP/azMy9oQxXvUve+oCJ93ynsiNYkfX477Zm/PsyZywFMlNd0r8kQD9zEj9XJv8F9X8rEDN08iNm1wCGQ4V1kGkEDc9m1YVZF4VisqZAwDM7lhQpkn9VokQGYQVTwdoKRfdr4A8yAg8Q8kQSdktzQfREDi4pQclcEn4J4FNvNiDAFZQW801rc6BbckB7c7oCBddxgVwyAyBXgyBuQMU2QeQYRbM4Q5BMATRSk8UyAUIMVjgeQyBpQ9lvQR8NI2AjReBAwdc9dYkyAIBwgDBhQKQy84Rw839GpEDo9kCX8ksyBc8X9sCfCSd/DV84919gcpRyofMBwy9P8T99xNC8U0it8do4RUDQiH8S9yDAisciCfgBx8j9wy9KCcEaC6D/dA8dRmDkMmY2Cy9i4mjgiHwVw+ZyxH4x5+C5AjJUAhCycWkq8a9+8B968h9G8w0NtEQNsUQCA0Rc1xj81C1gs2c3DAxsQKAYQbD0BnsFi4QK0ABpPDF8Y4jPOAY4pLY4sjU4hPWiCtR4NyOAQAJMJosXwxsTUBxaMzV9V8VjiyULjKVHg38K1jlCkG5WRYCzjfDMdXhniYSGRYDC9ywAAfCEope4OCaHVHKANE5tNExEwMSE7EveTEqEgkvIvea4oovjH0YgpAtLGk8vSvNVDzIGOBAeJBR4QAAIIGSfhAVZRfisMsBDjXgiSqQSSsSIBdwzhHgpS8TqQCSNFTj9wMTpSoTySz98SDNviJTiTSTZS95iS8SVSrjVoNSjScTYCCT6si415pYvjeFWJl17VtNy4KSyTYC6V+ilMf4cwT0z0L01Nb0/N9Mdo2S0AuxZQFSUS8VYCARnC4BJSvTZTaQzhbTm01SUy0ybSdS0SOSBi8TwyfQTUYyMQJAhhTAPQJS8ztSzTCT6z5SpTrTlTU5UzNTsSMzcTYdCz6TUAbBgABwrSZT8zGyNFRytT5TodrSCSOQiTZyxyGy+y6SsIutqhcyuzjTMyCyY5ywGQ0TWzlyZy8zaQOR/Ylzpzey0c7TgNQMWpHgY5qlJzmzQQrzsT5yUzDSTybz8TmYoMSSDoqkqkKzzhLAEQqYYAMlvgMoJRjhrjuQpyyTdyJzvzjyoSey8z+ygUyASAaUDSPydyiLBACTDy3yfzKSAL4M4knIoYQLCDyxmlP59VDJALIVNk3yUS4NoMOLulKKUKSLqQokdpRKdp2KkNLyuKdS+lpA7tG8GBHsF0gwEQnB7DZDSQaVlFkYw9YSIim0oi2DXgN84idpwTtzoSdS8N4i8TjN0xsF6dkcZKEyZL4jtiRzEdP0hLtS5zsC6BjgAJkizhEtUStzrSVydRzSJR/KupACgU3M8chsy1WQKRRtxtGiptAcDMxTUQRzpKJyY40TPKuMLKsKLKqTsYn8gNaJ1jcs7DtiN49iDjcrUrisviJtMqaxUAEri5YcDN/5XgxRU9mTgrWSRj2TywNzcdkLiLbSY5JzirT82yfKxyKrH9gqeNUAcrFjaIXzsYYqE4S9JpqSNq1yxLISSkB4uT2JEMBUtjgBTBByfRtj9yi0WLoydpqlj4DrJ0R5eiX4xiViJEtRkAhRwKQBIL9tTspiiQ+8gaxFB8lsiQHsnsvQwbtKItdLvtl8mTY8jKKNN9aJZQMVaQABVWQxwkeHnOASAE7NsZdMgcqSHP8tyBHWnLGRyv89HZywAciIib31NpRD/8J94BNLIRBQkRiAbc7cNySlOINAYAoFypAAAIhZvhxjh3zLwgNxnsrpycycqVPgLEp33/zv1yMqtGvKMCJjiSMqu/3/z/1/zgD5p2mJpDVpDwBhEKW4CrGgo9By1+EehitUPgsSy0j4KRB100vhDmO2rhGioCpVpIrVomREtEsWoNth25tsteMKozu8t3N8oWQOqCpI1zrEpmvHNXOLoCuqvLHxUUqexey2wJlYMBzTrsyRKgisOFqgScmn0YHgFZHnysrbolA7tYwspZt6sXyxD0MGkbuUue0RHUqQXBBk0IzYJnrJDnrICNyAA)

---

## Summary

This artifact provides a fully verified Lean 4 + Mathlib proof of three mathematical claims underpinning the CWA (Curie-Weiss Activation) scalar fixed-point iteration F(m) = tanh(x + J*m) for J in (0, 1).

**Theorem 1 — Banach Convergence (cwa_banach):** For any input x and coupling J in (0,1), there exists a unique m* satisfying tanh(x + J*m*) = m*. Proof chain: (i) derive HasDerivAt for sinh, cosh, tanh from first principles using HasDerivAt.inv + HasDerivAt.mul (since DerivHyp is broken and HasDerivAt.div is absent); (ii) prove sech^2 = 1 - tanh^2 in [0,1] via Real.cosh_sq_sub_sinh_sq + nlinarith; (iii) bound nnnorm of tanh's derivative by 1; (iv) apply lipschitzWith_of_nnnorm_deriv_le to get LipschitzWith 1 tanh; (v) compose with J-Lipschitz affine map to get LipschitzWith J F; (vi) form ContractingWith since J < 1; (vii) invoke ContractingWith.fixedPoint_isFixedPt + fixedPoint_unique.

**Theorem 2 — IFT Gradient Formula (ift_gradient_correct):** With s_bar = 1 - tanh^2(x + J*m*) and grad = s_bar/(1 - J*s_bar), the equation s_bar*(1 + J*grad) = grad holds. Proof: establish 1 - J*s_bar > 0, then field_simp closes the algebraic identity.

**Theorem 3 — Uniform Bias Bound (cwa_ift_bias_uniform):** If |F(m_approx) - m_approx| <= 1e-4*(1-J), then |m_approx - m*| <= 1e-4. Proof: contraction_residual_bound (triangle + Lipschitz) gives |error| <= |residual|/(1-J); substituting the tolerance yields 1e-4.

**Verified:** verified=true, has_sorries=false.

## Lean Code

```lean
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Topology.MetricSpace.Contracting

-- CWA Proof: convergence, IFT formula, and bias bound
-- Three theorems for F(m) = tanh(x + J*m), J in (0,1)

-- ============================================================
-- Part 1: Derivatives of sinh, cosh, tanh
-- ============================================================

lemma hasDerivAt_sinh (x : ℝ) : HasDerivAt Real.sinh (Real.cosh x) x := by
  have h1 := Real.hasDerivAt_exp x
  have h2 : HasDerivAt (Real.exp ∘ Neg.neg) (Real.exp (-x) * (-1)) x :=
    (Real.hasDerivAt_exp (-x)).comp x (hasDerivAt_neg x)
  have h4 : HasDerivAt (fun x => (Real.exp x - Real.exp (-x)) / 2)
      ((Real.exp x - Real.exp (-x) * (-1)) / 2) x :=
    (h1.sub h2).div_const 2
  convert h4 using 1
  · funext y; exact Real.sinh_eq y
  · rw [Real.cosh_eq]; ring

lemma hasDerivAt_cosh (x : ℝ) : HasDerivAt Real.cosh (Real.sinh x) x := by
  have h1 := Real.hasDerivAt_exp x
  have h2 : HasDerivAt (Real.exp ∘ Neg.neg) (Real.exp (-x) * (-1)) x :=
    (Real.hasDerivAt_exp (-x)).comp x (hasDerivAt_neg x)
  have h4 : HasDerivAt (fun x => (Real.exp x + Real.exp (-x)) / 2)
      ((Real.exp x + Real.exp (-x) * (-1)) / 2) x :=
    (h1.add h2).div_const 2
  convert h4 using 1
  · funext y; exact Real.cosh_eq y
  · rw [Real.sinh_eq]; ring

lemma hasDerivAt_tanh (x : ℝ) : HasDerivAt Real.tanh (1 - Real.tanh x ^ 2) x := by
  have hcosh_ne : Real.cosh x ≠ 0 := (Real.cosh_pos x).ne'
  have hsinh := hasDerivAt_sinh x
  have hcosh := hasDerivAt_cosh x
  have hcosh_inv : HasDerivAt (fun y => (Real.cosh y)⁻¹) (-Real.sinh x / Real.cosh x ^ 2) x :=
    hcosh.inv hcosh_ne
  have hprod : HasDerivAt (fun y => Real.sinh y * (Real.cosh y)⁻¹)
      (Real.cosh x * (Real.cosh x)⁻¹ + Real.sinh x * (-Real.sinh x / Real.cosh x ^ 2)) x :=
    hsinh.mul hcosh_inv
  convert hprod using 1
  · funext y; rw [Real.tanh_eq_sinh_div_cosh]; field_simp
  · rw [Real.tanh_eq_sinh_div_cosh]
    have hid : Real.cosh x ^ 2 - Real.sinh x ^ 2 = 1 := Real.cosh_sq_sub_sinh_sq x
    field_simp
    nlinarith [Real.cosh_pos x]

lemma differentiable_tanh : Differentiable ℝ Real.tanh :=
  fun x => (hasDerivAt_tanh x).differentiableAt

-- ============================================================
-- Part 2: tanh is 1-Lipschitz
-- ============================================================

lemma sech_sq_nonneg (x : ℝ) : 0 ≤ 1 - Real.tanh x ^ 2 := by
  have hid : Real.cosh x ^ 2 - Real.sinh x ^ 2 = 1 := Real.cosh_sq_sub_sinh_sq x
  have hcp := Real.cosh_pos x
  rw [Real.tanh_eq_sinh_div_cosh, div_pow,
      one_sub_div (pow_ne_zero 2 hcp.ne')]
  apply div_nonneg _ (sq_nonneg _)
  nlinarith [sq_nonneg (Real.sinh x)]

lemma sech_sq_le_one (x : ℝ) : 1 - Real.tanh x ^ 2 ≤ 1 := by
  linarith [sq_nonneg (Real.tanh x)]

lemma nnnorm_deriv_tanh_le (x : ℝ) : ‖deriv Real.tanh x‖₊ ≤ 1 := by
  rw [(hasDerivAt_tanh x).deriv]
  have h0 := sech_sq_nonneg x
  have h1 := sech_sq_le_one x
  rw [show ‖(1 - Real.tanh x ^ 2)‖₊ = ⟨1 - Real.tanh x ^ 2, h0⟩ from by
    simp [nnnorm, NNNorm.nnnorm, Real.norm_of_nonneg h0]]
  exact_mod_cast h1

lemma tanh_lipschitzWith_one : LipschitzWith 1 Real.tanh :=
  lipschitzWith_of_nnnorm_deriv_le differentiable_tanh nnnorm_deriv_tanh_le

-- ============================================================
-- Part 3: F(m) = tanh(x + J*m) is J-Lipschitz and contracting
-- ============================================================

lemma lin_lipschitz (x : ℝ) {J : ℝ} (hJ0 : 0 ≤ J) :
    LipschitzWith ⟨J, hJ0⟩ (fun m => x + J * m) := by
  rw [lipschitzWith_iff_dist_le_mul]
  intro a b
  simp only [Real.dist_eq, NNReal.coe_mk]
  have h : x + J * a - (x + J * b) = J * (a - b) := by ring
  rw [h, abs_mul, abs_of_nonneg hJ0]

lemma F_lipschitz (x : ℝ) {J : ℝ} (hJ0 : 0 ≤ J) (hJ1 : J < 1) :
    LipschitzWith ⟨J, hJ0⟩ (fun m => Real.tanh (x + J * m)) := by
  have h := tanh_lipschitzWith_one.comp (lin_lipschitz x hJ0)
  simp only [NNReal.coe_one, one_mul] at h
  have heq : Real.tanh ∘ (fun m => x + J * m) = fun m => Real.tanh (x + J * m) := rfl
  rwa [heq] at h

lemma F_contracting (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1) :
    ContractingWith ⟨J, le_of_lt hJ0⟩ (fun m => Real.tanh (x + J * m)) := by
  constructor
  · exact_mod_cast hJ1
  · exact F_lipschitz x (le_of_lt hJ0) hJ1

-- ============================================================
-- Theorem 1: CWA Banach Fixed-Point Theorem
-- ============================================================

theorem cwa_banach (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1) :
    ∃! m_star : ℝ, Real.tanh (x + J * m_star) = m_star := by
  have hc := F_contracting x hJ0 hJ1
  let F := fun m => Real.tanh (x + J * m)
  use ContractingWith.fixedPoint F hc
  exact ⟨hc.fixedPoint_isFixedPt, fun y hy => hc.fixedPoint_unique hy⟩

-- ============================================================
-- Part 4: Algebraic helpers for IFT
-- ============================================================

lemma one_sub_J_sbar_pos {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1)
    (s_bar : ℝ) (hs0 : 0 ≤ s_bar) (hs1 : s_bar ≤ 1) :
    0 < 1 - J * s_bar := by nlinarith

-- ============================================================
-- Theorem 2: IFT Gradient Formula
-- ============================================================

theorem ift_gradient_correct (x J m_star : ℝ) (hJ0 : 0 < J) (hJ1 : J < 1) :
    let s_bar := 1 - Real.tanh (x + J * m_star) ^ 2
    let grad := s_bar / (1 - J * s_bar)
    s_bar * (1 + J * grad) = grad := by
  simp only
  set s := 1 - Real.tanh (x + J * m_star) ^ 2
  have hs0 : 0 ≤ s := sech_sq_nonneg _
  have hs1 : s ≤ 1 := sech_sq_le_one _
  have hden : 1 - J * s ≠ 0 :=
    (one_sub_J_sbar_pos hJ0 hJ1 s hs0 hs1).ne'
  field_simp [hden]

-- IFT algebraic uniqueness: s*(1+J*d) = d implies d = s/(1-J*s)
lemma ift_equation_unique_solution (s_bar d J : ℝ)
    (hs0 : 0 ≤ s_bar) (hs1 : s_bar ≤ 1)
    (hJ0 : 0 < J) (hJ1 : J < 1)
    (heq : s_bar * (1 + J * d) = d) :
    d = s_bar / (1 - J * s_bar) := by
  have hden : 1 - J * s_bar ≠ 0 :=
    (one_sub_J_sbar_pos hJ0 hJ1 s_bar hs0 hs1).ne'
  field_simp [hden]
  linarith

-- ============================================================
-- Theorem 3: Bias Bound
-- ============================================================

lemma contraction_residual_bound {K : ℝ} (hK0 : 0 ≤ K) (hK1 : K < 1)
    {f : ℝ → ℝ} (hf_lip : LipschitzWith ⟨K, hK0⟩ f)
    {m_approx m_star : ℝ} (hstar : f m_star = m_star) :
    |m_approx - m_star| ≤ |f m_approx - m_approx| / (1 - K) := by
  have hden : 0 < 1 - K := by linarith
  rw [le_div_iff₀ hden]
  -- Lipschitz bound: |f(m_approx) - f(m_star)| ≤ K * |m_approx - m_star|
  have hlip : |f m_approx - f m_star| ≤ K * |m_approx - m_star| := by
    have h := hf_lip.dist_le_mul m_approx m_star
    simp only [Real.dist_eq, NNReal.coe_mk] at h
    linarith
  -- f(m_star) = m_star, so |f(m_approx) - m_star| ≤ K * |m_approx - m_star|
  rw [hstar] at hlip
  -- Triangle: |m_approx - m_star| ≤ |m_approx - f(m_approx)| + |f(m_approx) - m_star|
  have htri : |m_approx - m_star| ≤ |m_approx - f m_approx| + |f m_approx - m_star| := by
    calc |m_approx - m_star|
        = |(m_approx - f m_approx) + (f m_approx - m_star)| := by ring_nf
      _ ≤ |m_approx - f m_approx| + |f m_approx - m_star| := abs_add _ _
  -- Combine to get (1-K)*|m_approx - m_star| ≤ |f(m_approx) - m_approx|
  have hsym : |f m_approx - m_approx| = |m_approx - f m_approx| := abs_sub_comm _ _
  nlinarith [abs_nonneg (m_approx - m_star), abs_nonneg (f m_approx - m_approx),
             abs_nonneg (f m_approx - m_star)]

theorem cwa_ift_bias_uniform (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1)
    {m_approx m_star : ℝ}
    (hstar : Real.tanh (x + J * m_star) = m_star)
    (hres : |Real.tanh (x + J * m_approx) - m_approx| ≤ 1e-4 * (1 - J)) :
    |m_approx - m_star| ≤ 1e-4 := by
  have hfl := F_lipschitz x (le_of_lt hJ0) hJ1
  have hbound : |m_approx - m_star| ≤
      |Real.tanh (x + J * m_approx) - m_approx| / (1 - J) :=
    contraction_residual_bound (le_of_lt hJ0) hJ1 hfl hstar
  have hpos : (0 : ℝ) < 1 - J := by linarith
  calc |m_approx - m_star|
      ≤ |Real.tanh (x + J * m_approx) - m_approx| / (1 - J) := hbound
    _ ≤ (1e-4 * (1 - J)) / (1 - J) := by
        apply div_le_div_of_nonneg_right hres
        linarith
    _ = 1e-4 := by field_simp

-- ============================================================
-- Main Combined Theorem
-- ============================================================

theorem cwa_main (x : ℝ) {J : ℝ} (hJ0 : 0 < J) (hJ1 : J < 1) :
    -- (1) Unique fixed point exists
    (∃! m_star : ℝ, Real.tanh (x + J * m_star) = m_star) ∧
    -- (2) IFT gradient formula is algebraically consistent
    (∀ m_star : ℝ,
      let s_bar := 1 - Real.tanh (x + J * m_star) ^ 2
      let grad := s_bar / (1 - J * s_bar)
      s_bar * (1 + J * grad) = grad) ∧
    -- (3) Adaptive tolerance 1e-4*(1-J) yields uniform bias bound 1e-4
    (∀ m_approx m_star : ℝ,
      Real.tanh (x + J * m_star) = m_star →
      |Real.tanh (x + J * m_approx) - m_approx| ≤ 1e-4 * (1 - J) →
      |m_approx - m_star| ≤ 1e-4) :=
  ⟨cwa_banach x hJ0 hJ1,
   fun m_star => ift_gradient_correct x J m_star hJ0 hJ1,
   fun m_approx m_star hstar hres => cwa_ift_bias_uniform x hJ0 hJ1 hstar hres⟩

```

---
*Generated by AI Inventor Pipeline*
