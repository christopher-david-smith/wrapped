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
      url:
        values.url === undefined
          ? null
          : values.url.match(/^https?:\/\/.*/i) || values.url.length == 0
            ? null
            : "Invalid URL",
      image:
        values.image === undefined
          ? null
          : values.image.match(/^https?:\/\/.*/i) || values.image.length == 0
            ? null
            : "Invalid image URL"
    })
  })

  useEffect(() => {
    API.Gifts.all().then((data) => {
      setGifts(data);
    });
  }, []);

  return (
    <div>
      <ResponseiveGrid minWidth={300}>
        {gifts.map((gift) => (
          <Gift
            {...gift}
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
        <form onSubmit={form.onSubmit((values) => console.log(values))}>
          <TextInput
            withAsterisk
            label="name"
            placeholder="Name..."
            key={form.key('name')}
            {...form.getInputProps('name')}
          />
          <TextInput
            mt={20}
            label="URL"
            placeholder="http://..."
            key={form.key('ur')}
            {...form.getInputProps('url')}
          />
          <TextInput
            mt={20}
            label="Image"
            placeholder="http://..."
            key={form.key('image')}
            {...form.getInputProps('image')}
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
