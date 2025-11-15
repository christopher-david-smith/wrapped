import { GiftProps } from "../components/Gifts/Gifts";

function loadList<T>(storageKey: string): T[] {
  try {
    const raw = localStorage.getItem(storageKey);
    return raw ? (JSON.parse(raw) as T[]) : [];
  } catch {
    return [];
  }
}

function saveList<T>(storageKey: string, items: T[]): void {
  localStorage.setItem(storageKey, JSON.stringify(items))
}

const STORAGE_KEYS = {
  gifts: "wrapped.gifts"
}

export const API = {
  Gifts: {

    async list(): Promise<GiftProps[]> {
      return loadList<GiftProps>(STORAGE_KEYS.gifts);
    },

    async add(data: Omit<GiftProps, "id" | "createdAt">): Promise<GiftProps> {
      const gift: GiftProps = {
        ...data,
        id: crypto.randomUUID(),
        createdAt: new Date().toISOString(),
      }

      const all = loadList<GiftProps>(STORAGE_KEYS.gifts);
      const next = [...all, gift];
      saveList(STORAGE_KEYS.gifts, next);

      return gift;
    },

    async delete(id: string): Promise<void> {
      const all = loadList<GiftProps>(STORAGE_KEYS.gifts);
      const filtered = all.filter((item) => item.id !== id);
      saveList(STORAGE_KEYS.gifts, filtered);
    }

  }
}
