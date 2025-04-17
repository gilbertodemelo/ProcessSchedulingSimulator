"""
put(chave, valor) – Adiciona ou atualiza um par chave → valor
get(chave) – Retorna o valor associado a uma chave
remove(chave) – Remove a chave e seu valor correspondente
contains_key(chave) – Verifica se a chave existe
keys() – Retorna todas as chaves
values() – Retorna todos os valores
items() – Retorna lista de pares (chave, valor)
size() – Retorna o número de pares armazenados
clear() – Remove todos os pares
is_empty() – Verifica se o Map está vazio
update(outro_map) – Adiciona/atualiza pares de outro Map
copy() – Retorna uma cópia do Map atual
invert() – Inverte chave ↔ valor (atenção com valores duplicados)

"""


class Map:

    def __init__(self):
        self._keys = []
        self._values = []
        self._size = 0


    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    @property
    def keys(self):
        if self.is_empty():
            raise Exception("Map is empty.")
        else:
            return self._keys

    @property
    def values(self):
        if self.is_empty():
            raise Exception("Map is empty.")
        else:
            return self._values

    @property
    def items(self):
        if self.is_empty():
            raise Exception("Map is empty.")
        else:
            res = []
            for i in range(len(self._keys)):
                res.append((self._keys[i], self._values[i]))
        return res

    def put(self, k, v):
        if k in self._keys:
            index = self._keys.index(k)
            self._values[index] = v
        else:
            self._keys.append(k)
            self._values.append(v)
            self._size += 1

    def get(self, k):
        if not self.is_empty():
            for i in range(len(self._keys)):
                if self._keys[i] == k:
                    return self._values[i]
        else:
            raise Exception("Map is empty.")

    def remove(self, k):
        if self.is_empty():
            raise Exception("Map is empty.")
        else:
            for i in range(len(self._keys)):
                if self._keys[i] == k:
                    self._keys.pop(i)
                    self._values.pop(i)
            self._size -= 1

    def contains_key(self, k):
        if self.is_empty():
            raise Exception("Map is empty.")
        else:
            return self._keys.__contains__(k)

    def clear(self):
        if not self.is_empty():
            self._keys = []
            self._values = []
        else:
            raise Exception("Map is empty.")


