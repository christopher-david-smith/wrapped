import { ResponseiveGrid } from "../components/ResponsiveGrid/ResponsiveGrid";
import { Gift, GiftProps } from "../components/Gifts/Gifts";
import { Group, ActionIcon, Button, Modal, TagsInput, TextInput } from "@mantine/core";
import { useState, useEffect } from "react";
import { useForm } from "@mantine/form";
import { API } from "../api/client";

export default function IdeasPage() {

  const [gifts, setGifts] = useState<GiftProps[]>([]);
  const [opened, setOpened] = useState(false);

  const form = useForm({
    mode: 'uncontrolled',
    validate: (values) => ({
      name:
        values.name === undefined
          ? "Name cannot be empty"
          : values.name.length == 0
            ? "Name cannot be empty"
            : null,
    })
  })

  async function loadGifts() {
    API.Gifts.all().then((data) => {
      setGifts(data);
    })
  }

  async function addGift(data: any) {
    API.Gifts.add(data).then(() => {
      loadGifts();
    })
  }

  async function deleteGift(id: number) {
    API.Gifts.delete(id).then(() => {
      loadGifts();
    })
  }

  useEffect(() => {
    loadGifts();
  }, []);

  return (
    <div>
      <ResponseiveGrid minWidth={300}>
        {gifts.map((gift) => (
          <Gift
            {...gift}
            onDelete={deleteGift}
          />
        ))}
      </ResponseiveGrid>
      <Modal
        opened={opened}
        onClose={() => setOpened(false)}
        title="Add new gift"
        centered
        radius="md"
      >
        <form
          onSubmit={form.onSubmit((values) => {
            addGift(values);
            setOpened(false);
          })}
        >
          <TextInput
            withAsterisk
            label="name"
            placeholder="Name..."
            key={form.key('name')}
            {...form.getInputProps('name')}
          />
          <TagsInput
            mt={20}
            label="Labels"
            key={form.key('labels')}
            {...form.getInputProps('labels')}
          />
          <Group justify="flex-end" mt="md">
            <Button type="submit">Submit</Button>
          </Group>
        </form>
      </Modal>
      <ActionIcon
        size="xl"
        radius="xl"
        color="blue"
        variant="filled"
        onClick={() => setOpened(true)}
        style={{
          position: "fixed",
          bottom: "24px",
          right: "24px",
          zIndex: 1000
        }}
      >
        +
      </ActionIcon>
    </div >
  )
}
