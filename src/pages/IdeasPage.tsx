import { ResponseiveGrid } from "../components/ResponsiveGrid/ResponsiveGrid";
import { Gift } from "../components/Gifts/Gifts";

export default function IdeasPage() {
  return (
    <div>
      <ResponseiveGrid minWidth={300}>
        <Gift name="test" description="Here is a description" />
        <Gift name="test" />
        <Gift name="test" />
        <Gift name="test" />
        <Gift name="test" />
      </ResponseiveGrid>
    </div >
  )
}
