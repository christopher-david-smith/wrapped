import { ResponseiveGrid } from "../components/ResponsiveGrid/ResponsiveGrid";
import { Gift } from "../components/Gifts/Gifts";
import { Group, ActionIcon, Button, Modal, TagsInput, TextInput } from "@mantine/core";
import { useState } from "react";
import { useForm } from "@mantine/form";

const gifts = [
  {
    "name": "Footballs",
    "handedOutCount": 1,
  },
  {
    "name": "New Computer"
  },
  {
    "name": "Christmas Tree",
  }
]

export default function IdeasPage() {
  const [opened, setOpened] = useState(false);
  const form = useForm({
    mode: 'uncontrolled',
    validate: {
      name: (value) => (/.+/.test(value) ? null : 'Name cannot be empty'),
      url: (value) => (/^https?:\/\/.*/.test(value) ? null : 'Invalid URL'),
      image: (value) => (/^https?:\/\/.*/.test(value) ? null : 'Invalid URL')
    }
  })
  return (
    <div>
      <ResponseiveGrid minWidth={300}>
        {gifts.map((gift) => (
          <Gift
            name={gift.name}
            ideaHandedOutCount={gift.handedOutCount}
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
