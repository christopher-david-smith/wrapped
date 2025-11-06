import { Card, Text, Group, Badge } from "@mantine/core";

interface GiftProps {
  name: string;
  url?: string;
  description?: string;
  image?: string;
  labels?: string[];
  ideaHandedOutCount?: number;
}

export const Gift = (props: GiftProps) => {
  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Text fw={700} size="lg">
        {props.name}
      </Text>
      {props.description &&
        <Text c="dimmed" size="md">
          {props.description}
        </Text>
      }
    </Card>
  )
}
