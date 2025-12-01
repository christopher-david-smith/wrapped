import { IconTrash } from "@tabler/icons-react";
import { Card, Text, Group, ActionIcon } from "@mantine/core";

export interface GiftProps {
  id: number;
  createdAt: string;
  name: string;
  labels?: string[];
  ideaHandedOutCount?: number;
  onDelete: (id: number) => void | Promise<void>;
}

export const Gift = (props: GiftProps) => {
  const handedOut: boolean = (props.ideaHandedOutCount ?? 0) > 0;
  return (
    <Card
      shadow="sm"
      padding="md"
      radius="md"
      withBorder
    >
      <Card.Section withBorder inheritPadding py="md">
        <Text fw={700} size="lg">
          {props.name}
        </Text>
      </Card.Section>
      <Group gap="xs" mt="lg">
        <ActionIcon
          component="a"
          variant="filled"
          color="red"
          onClick={() => props.onDelete(props.id)}
        >
          <IconTrash />
        </ActionIcon>
      </Group>
    </Card >
  )
}
